import React, { useEffect, useState } from "react";
import axios from "axios";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import styles from "../../styles/Post.module.css";
import { Card, Media, OverlayTrigger, Tooltip } from "react-bootstrap";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";

//working version
//working version

const Post = (props) => {
    const { id, title, content, image, updated_at, profile_id, profile_image, user, likes_count, comments_count, like_id, postPage, setPosts } = props;
    const currentUser = useCurrentUser();
    const [userRating, setUserRating] = useState(null);
    const [averageRating, setAverageRating] = useState(null);
    const is_owner = currentUser?.username === user;


    useEffect(() => {
        if (typeof id === 'undefined') {
            console.log('Recipe ID is undefined, skipping fetch.');
            return;
        }
        const fetchRatings = async () => {
            try {
                const { data } = await axios.get(`/ratings/?recipe=${id}`);
                console.log('Fetched ratings data:', data); // Log fetched data
                const currentRecipeRatings = data.results.filter(rating => rating.recipe === id);
    
                // find if the current user has rated this recipe.
                const userRatingData = currentRecipeRatings.find(rating => rating.is_user);
                if (userRatingData) {
                    // If the current user has rated, use this rating.
                    setUserRating(userRatingData.your_rating);
                    setAverageRating(userRatingData.recipe_average_rating);
                } else {
                    // If the current user has not rated, use the average rating.
                    const avgRating = currentRecipeRatings.length ? currentRecipeRatings[0].recipe_average_rating : null;
                    setAverageRating(avgRating);
                }
                console.log('User rating:', userRatingData ? userRatingData.your_rating : 'Not rated by user'); // Log user rating
                console.log('Average rating:', averageRating); // Log average rating
            } catch (err) {
                console.error("Failed to fetch ratings:", err);
            }
        };
    
        fetchRatings();
    }, [id, currentUser]);
    
    const handleRating = async (rating) => {
        if (!currentUser) {
            alert("Please log in to rate.");
            return;
        }
        if (userRating !== null) {
            alert("You have already rated this recipe.");
            return;
        }
    
        try {
            const method = userRating ? "patch" : "post";
            const response = await axios[method](`/ratings/${userRating ? userRating.id : ''}`, {
                recipe: id,
                your_rating: rating, // The rating the user wants to give
            });
    
            setUserRating(rating);
            setAverageRating(response.data.recipe_average_rating);
            console.log('Rating submission successful:', response.data); // Log successful rating submission
            alert("You rated this recipe successfully.");
        } catch (error) {
            console.error("Rating submission error:", error);
            if (error.response && error.response.data.your_rating) {
                alert(error.response.data.your_rating[0]);
            } else {
                alert("You have already rated this recipe.");
            }
        }
    };
    
    const renderStars = () => {
        // Default to 0 if no rating is available
        const ratingToShow = typeof userRating === 'number' ? userRating : averageRating || 0;
        console.log('Rating to show with stars:', ratingToShow); // Log rating used for displaying stars
    
        return [1, 2, 3, 4, 5].map(star => (
            <i key={star}
                className={`fa fa-star ${star <= ratingToShow ? "checked" : ""}`}
                onClick={() => handleRating(star)}
                style={{
                    cursor: userRating === null ? "pointer" : "default",
                    color: star <= ratingToShow ? "#ffc107" : "#e4e5e9",
                    marginRight: 5
                }}
            />
        ));
    };

    const handleLike = async () => {
        try {
            const { data } = await axiosRes.post("/likes/", { post: id });
            setPosts((prevPosts) => ({
                ...prevPosts,
                results: prevPosts.results.map((post) => {
                    if (post.id === id) {
                        // Ensure likes_count is treated as a number, defaulting to 0 if undefined
                        const updatedLikesCount = (post.likes_count || 0) + 1;
                        return { ...post, likes_count: updatedLikesCount, like_id: data.id };
                    }
                    return post;
                }),
            }));
        } catch (err) {
            console.log(err);
        }
    };
    
    const handleUnlike = async () => {
        try {
            await axiosRes.delete(`/likes/${like_id}/`);
            setPosts((prevPosts) => ({
                ...prevPosts,
                results: prevPosts.results.map((post) => {
                    if (post.id === id) {
                        // Ensure likes_count is treated as a number, defaulting to 0 if undefined
                        const updatedLikesCount = (post.likes_count || 1) - 1;
                        return { ...post, likes_count: updatedLikesCount, like_id: null };
                    }
                    return post;
                }),
            }));
        } catch (err) {
            console.log(err);
        }
    };



    return (
        <Card className={styles.Post}>
            <Card.Body>
                <Media className="align-items-center justify-content-between">
                    <Link to={`/profiles/${profile_id}`}>
                        <Avatar src={profile_image} height={55} />
                        {user}
                    </Link>
                    <div className="d-flex align-items-center">
                        <span>{updated_at}</span>
                        {is_owner && postPage && "..."}
                    </div>
                </Media>
            </Card.Body>
            <Link to={`/recipe-posts/${id}`}>
                <Card.Img src={image} alt={title} />
            </Link>
            <Card.Body>
                {title && <Card.Title className="text-center">{title}</Card.Title>}
                {content && <Card.Text>{content}</Card.Text>}
                <div>Average Rating: {averageRating}</div>
                <div className={styles.PostBar}>{renderStars()}</div>
                <div>{userRating !== null ? `You have already rated this recipe` : 'You have not rated this recipe yet.'}</div>

                <div className={styles.PostBar}>
                    {is_owner ? (
                        <OverlayTrigger
                            placement="top"
                            overlay={<Tooltip>You can't like your own post!</Tooltip>}
                        >
                            <i className="far fa-heart" />
                        </OverlayTrigger>
                    ) : like_id ? (
                        <span onClick={(handleUnlike)}>
                            <i className={`fas fa-heart ${styles.Heart}`} />
                        </span>
                    ) : currentUser ? (
                        <span onClick={(handleLike)}>
                            <i className={`far fa-heart ${styles.HeartOutline}`} />
                        </span>
                    ) : (
                        <OverlayTrigger
                            placement="top"
                            overlay={<Tooltip>Log in to like posts!</Tooltip>}
                        >
                            <i className="far fa-heart" />
                        </OverlayTrigger>
                    )}
                    {likes_count}
                    <Link to={`/posts/${id}`}>
                        <i className="far fa-comments" />
                    </Link>
                    {comments_count}
                </div>
            </Card.Body>
        </Card>
    );
};

export default Post;
