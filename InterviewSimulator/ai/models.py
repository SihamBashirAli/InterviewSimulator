from django.db import models
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def train_model():
    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train a simple logistic regression model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Save the model
    np.save('ai/model.npy', model)

    # Evaluate the model
    score = model.score(X_test, y_test)
    return score

