import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Upload from "../../assets/upload.png";
import styles from "../../styles/PostCreateEditForm.module.css";
import appStyles from "../../App.module.css";
import btnStyles from "../../styles/Button.module.css";
import Asset from "../../components/Asset";
import { Image } from "react-bootstrap";

function PostCreateForm() {
    const [postData, setPostData] = useState({
        title: "",
        content: "",
        image: "",
    });
    const { title, content, image } = postData;

    const handleChange = (event) => {
        setPostData({
            ...postData,
            [event.target.name]: event.target.value,
        });
    };

    const handleChangeImage = (event) => {
        if (event.target.files.length) {
            URL.revokeObjectURL(image);
            setPostData({
                ...postData,
                image: URL.createObjectURL(event.target.files[0]),
            });
        }
    };

    return (
        <Container className={`${appStyles.Content} ${styles.Container} mt-3`}>
            <Form>
                <Form.Group controlId="image-upload" className="text-center">
                    {image ? (
                        <>
                            <figure>
                                <Image className={appStyles.Image} src={image} rounded />
                            </figure>
                            <div>
                                <Form.Label
                                    className={`${btnStyles.Button} ${btnStyles.Blue} btn`}
                                    htmlFor="image-upload"
                                >
                                    Change the image
                                </Form.Label>
                            </div>
                        </>
                    ) : (
                        <Form.Label
                            className="d-flex justify-content-center"
                            htmlFor="image-upload"
                        >
                            <Asset src={Upload} message="Click or tap to upload an image" />
                        </Form.Label>
                    )}
                    <Form.Control
                        type="file"
                        onChange={handleChangeImage}
                        hidden
                        accept="image/*"
                    />
                </Form.Group>

                <Form.Group controlId="formPostTitle">
                    <Form.Label>Title</Form.Label>
                    <Form.Control
                        type="text"
                        name="title"
                        value={title}
                        onChange={handleChange}
                        placeholder="Enter title"
                    />
                </Form.Group>

                <Form.Group controlId="formPostContent">
                    <Form.Label>Content</Form.Label>
                    <Form.Control
                        as="textarea"
                        rows={6}
                        name="content"
                        value={content}
                        onChange={handleChange}
                        placeholder="Write your post content here..."
                    />
                </Form.Group>

                <div className="text-center">
                    <Button variant="dark" className={`${btnStyles.Button}`} onClick={() => { }} ><span className={btnStyles.buttonText}>Cancel</span>
                    </Button>
                    <Button
                        variant="dark" className={`${btnStyles.Button}`}
                        type="submit"
                    ><span className={btnStyles.buttonText}>Create</span>
                    </Button>
                </div>
            </Form>
        </Container>
    );
}

export default PostCreateForm;
