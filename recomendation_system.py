from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:
    def __init__(self, items: List[dict], feature_key: str = "genre") -> None:
        """
        Initialize the recommender with items and feature key.

        Args:
            items (List[dict]): List of items, each item is a dict with keys including title and features.
            feature_key (str): The key to extract features for similarity (default: 'genre').
        """
        self.items = items
        self.feature_key = feature_key
        self.titles = [item["title"] for item in items]
        self.features = [item[feature_key] for item in items]

        self.vectorizer = TfidfVectorizer()
        self.feature_vectors = self.vectorizer.fit_transform(self.features)

    def recommend(self, liked_title: str, top_n: int = 5) -> List[str]:
        """
        Recommend top_n similar items based on the liked_title.

        Args:
            liked_title (str): The title of the item user likes.
            top_n (int): Number of recommendations to return.

        Returns:
            List[str]: List of recommended item titles.
        """
        if liked_title not in self.titles:
            raise ValueError(f"Item '{liked_title}' not found in the database.")

        idx = self.titles.index(liked_title)
        similarity_scores = cosine_similarity(self.feature_vectors[idx], self.feature_vectors).flatten()

        # Exclude the liked item itself by setting its score to -1
        similarity_scores[idx] = -1

        top_indices = similarity_scores.argsort()[::-1][:top_n]

        return [self.titles[i] for i in top_indices]


if __name__ == "__main__":
    # Dataset example: movies with genre features
    movie_dataset = [
        {"title": "Inception", "genre": "sci-fi thriller dream"},
        {"title": "The Matrix", "genre": "sci-fi action reality"},
        {"title": "Interstellar", "genre": "sci-fi space drama"},
        {"title": "The Notebook", "genre": "romance drama love"},
        {"title": "Titanic", "genre": "romance drama ship"},
        {"title": "Avengers", "genre": "action superhero marvel"},
    ]

    recommender = ContentBasedRecommender(movie_dataset)

    try:
        recommendations = recommender.recommend("Inception", top_n=3)
        print(f"Recommendations based on 'Inception':")
        for rec in recommendations:
            print(f" - {rec}")
    except ValueError as e:
        print(e)
