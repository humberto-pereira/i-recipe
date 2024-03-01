import React, { useState, useEffect } from 'react';
import { axiosReq } from '../api/axiosDefaults'; 



const RatingComponent = ({ postId, initialAverageRating, userRating, onRatingSuccess, rating_id }) => {
    const [averageRating, setAverageRating] = useState(initialAverageRating);
    const [hasRated, setHasRated] = useState(false);

    useEffect(() => {
        console.log("Initial Props:", { postId, initialAverageRating, userRating, rating_id});
        setAverageRating(initialAverageRating);
        setHasRated(!!userRating);
    }, [postId, initialAverageRating, userRating, rating_id]);

    useEffect(() => {
        if (userRating) {
            setHasRated(true);
            // If there's a userRating already, it means the user has rated.
        }
        console.log("Received userRating: ", userRating);
    }, [userRating]);

    const handleRating = async (newRating) => {
        console.log("Current userRating:", userRating);
        let url, method;
        
        if (hasRated) {
            // User has already rated, so we update the existing rating
            url = `/ratings/${rating_id}/`; // Use rating_id directly
            console.log("Updating existing rating", {rating_id});
            method = 'patch';
            console.log("Updating existing rating");
        } else {
            // No existing rating, so we create a new one
            url = `/ratings/`;
            method = 'post';
            console.log("Creating new rating");
        }
    
        const body = { recipe: postId, your_rating: newRating };
        console.log('Post id', {postId});
    
        try {
            const response = await axiosReq[method](url, body);
            if (response.status === 200 || response.status === 201) {
                setAverageRating(response.data.recipe_average_rating);
                onRatingSuccess(response.data.recipe_average_rating);
                // After a successful rating, ensure we reflect that the user has now rated.
                setHasRated(true);
            }
        } catch (error) {
            console.error("Error handling rating", error);
        }
    };
    

    const renderStars = () => {
        return [1, 2, 3, 4, 5].map((star) => (
            <i key={star}
                className={`fa fa-star ${star <= averageRating ? "checked" : ""}`}
                onClick={() => handleRating(star)}
                style={{
                    cursor: hasRated ? "default" : "pointer",
                    color: star <= averageRating ? "#ffc107" : "#e4e5e9",
                    marginRight: "5px",
                }}
            ></i>
        ));
    };

    return (
        <div>
            {renderStars()}
        </div>
    );
};

export default RatingComponent;
