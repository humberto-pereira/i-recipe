import React, { useEffect, useState } from "react";

import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import appStyles from "../../App.module.css";
import { useParams } from "react-router";
import { axiosReq } from "../../api/axiosDefaults";
import Post from "./Post";
import Comment from "../comments/Comment";
import CommentCreateForm from "../comments/CommentCreateForm";
import { useCurrentUser } from "../../contexts/CurrentUserContext";

function RecipePostPage() {
    const { id } = useParams();
    const [post, setPost] = useState({ results: [] });
    const currentUser = useCurrentUser();

    const profile_image = currentUser?.profile_image;
    const [comments, setComments] = useState({ results: [] });

    useEffect(() => {
        const handleMount = async () => {
            try {
                // Fetch both post and comments data
                const [postResponse, commentsResponse] = await Promise.all([
                    axiosReq.get(`/recipe-posts/${id}`),
                    axiosReq.get(`/comments/?post=${id}`), 
                ]);
                console.log("Post fetched: ", postResponse.data);
                console.log("Comments fetched: ", commentsResponse.data);
                
                // Update states with fetched data
                setPost({ results: [postResponse.data] });
                setComments(commentsResponse.data); 
            } catch (err) {
                console.log(err);
            }
        };
    
        handleMount();
    }, [id]);

    return (
        <Row className="h-100">
            <Col className="py-2 p-0 p-lg-2" lg={8}>
                <p>Popular profiles for mobile</p>
                <Post {...post.results[0]} setPosts={setPost} postPage />
                <Container className={appStyles.Content}>{currentUser ? (
                    <CommentCreateForm
                        profile_id={currentUser.profile_id}
                        profileImage={profile_image}
                        post={id}
                        setPost={setPost}
                        setComments={setComments}
                    />
                ) : comments.results.length ? (
                    "Comments"
                ) : null}
                    {comments.results.length ? (
                        comments.results.map((comment) => (
                            <p key={comment.id}>
                                {comment.user} : {comment.content}
                            </p>
                        ))
                    ) : currentUser ? (
                        <span>No comments yet, be the first to comment!</span>
                    ) : (
                        <span>No comments... yet</span>
                    )}
                </Container>
            </Col>
            <Col lg={4} className="d-none d-lg-block p-0 p-lg-2">
                Popular profiles for desktop
            </Col>
        </Row>
    );
}

export default RecipePostPage;