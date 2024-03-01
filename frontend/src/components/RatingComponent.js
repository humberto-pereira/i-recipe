import React, { useState, useEffect } from 'react';
import { axiosReq } from '../api/axiosDefaults'; 



const RatingComponent = ({ postId, initialAverageRating, userRating, onRatingSuccess, rating_id }) => {
    const [averageRating, setAverageRating] = useState(initialAverageRating);
    const [hasRated, setHasRated] = useState(false);

    useEffect(() => {
        setAverageRating(initialAverageRating);
        setHasRated(!!userRating);
    }, [postId, initialAverageRating, userRating, rating_id]);

    useEffect(() => {
        if (userRating) {
            setHasRated(true);
            // If there's a userRating already, it means the user has rated.
        }
    }, [userRating]);

    const handleRating = async (newRating) => {
        let url, method;
        
        if (hasRated) {
            // User has already rated, so update the existing rating
            url = `/ratings/${rating_id}/`; // Use rating_id directly
            method = 'patch';
        } else {
            // No existing rating, so create a new one
            url = `/ratings/`;
            method = 'post';
        }
    
        const body = { recipe: postId, your_rating: newRating };
        try {
            const response = await axiosReq[method](url, body);
            if (response.status === 200 || response.status === 201) {
                setAverageRating(response.data.recipe_average_rating);
                onRatingSuccess(response.data.recipe_average_rating);
                // After a successful rating, ensure it reflect that the user has now rated.
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
