import React, { useRef, useState, useEffect } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Alert from "react-bootstrap/Alert";
import Upload from "../../assets/upload.png";
import styles from "../../styles/PostCreateEditForm.module.css";
import appStyles from "../../App.module.css";
import btnStyles from "../../styles/Button.module.css";
import Asset from "../../components/Asset";
import { Image } from "react-bootstrap";

function PostCreateForm() {
    const [errors, setErrors] = useState({});
    const [categories, setCategories] = useState([]);
    const [tags, setTags] = useState([]);

    const [postData, setPostData] = useState({
        title: "",
        content: "",
        image: "",
        category: "",
        tag: "",
    });
    const { title, content, image, category, tag } = postData;

    const imageInput = useRef(null);
    const history = useHistory();

    useEffect(() => {
        async function fetchCategoriesAndTags() {
            try {
                const categoriesResponse = await axios.get("/categories/");
                setCategories(categoriesResponse.data.results);

                const tagsResponse = await axios.get("/tag-choices/");
                // Directly transform tagsResponse.data into an array of objects for easier mapping
                const tagsArray = Object.entries(tagsResponse.data).map(([key, value]) => ({
                    value: key,
                    label: value,
                }));
                setTags(tagsArray);
            } catch (err) {
                console.error("Error fetching categories or tags:", err);
                setCategories([]);
                setTags([]);
            }
        }

        fetchCategoriesAndTags();
    }, []);

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

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();

        formData.append("title", title);
        formData.append("content", content);
        formData.append("category", category);
        formData.append("tags", tag);
        formData.append("image", imageInput.current.files[0]);

        try {
            const { data } = await axios.post("/recipe_posts/", formData);
            history.push(`/recipe-posts/${data.id}`);
        } catch (err) {
            console.log(err);
            if (err.response?.status !== 401) {
                setErrors(err.response?.data);
            }
        }
    };

    return (
        <Container className={`${appStyles.Content} ${styles.Container} mt-3`}>
            <Form onSubmit={handleSubmit}>
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
                        ref={imageInput}
                    />
                </Form.Group>
                

                <Form.Group controlId="formCategory">
                    <Form.Label>Category</Form.Label>
                    <Form.Control as="select" name="category" value={category} onChange={handleChange}>
                        <option value="">Select a Category</option>
                        {categories.map((c) => (
                            <option key={c.id} value={c.id}>{c.name}</option>
                        ))}
                    </Form.Control>
                </Form.Group>
                {errors?.category?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}

                <Form.Group controlId="formPostTags">
                    <Form.Label>Tags</Form.Label>
                    <Form.Control as="select" name="tag" value={tag} onChange={handleChange}>
                        <option value="">Select a Tag</option>
                        {tags.map((tag, index) => (
                            <option key={index} value={tag.value}>{tag.label}</option>
                        ))}
                    </Form.Control>
                </Form.Group>
                {errors?.tags?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}

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
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}

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
                {errors?.content?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}

                <div className="text-center">
                    <Button variant="dark" className={`${btnStyles.Button}`} onClick={() => history.goBack()} ><span className={btnStyles.buttonText}>Cancel</span>
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
