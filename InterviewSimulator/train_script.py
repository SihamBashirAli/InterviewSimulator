import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    print("Training model...")
    
    # Example training data
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([2, 3, 4, 5])
    
    print("Training data loaded.")
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print("Model training complete.")
    
    # Save the model
    joblib.dump(model, 'ai_model.pkl')
    
    print("Model saved as 'ai_model.pkl'")

if __name__ == "__main__":
    train_model()
