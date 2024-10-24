import numpy as np
import pickle

# Load the trained model
with open("models/trained_model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_mood(features):
    """
    Predicts the mood score based on the input features.

    Parameters:
    features (list): A list containing 4 input features (anxiety, depression, schizophrenia, bipolar).

    Returns:
    float: The predicted mood score.
    """
    # The model expects 12 features. We add 8 default features
    complete_features = features + [0] * 8  # Adding 8 zeros

    # Convert the features list to a NumPy array
    features_array = np.array([complete_features])

    # Make prediction
    mood_score = model.predict(features_array)[0]

    return mood_score
