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
    complete_features = (
        features + [0] * 8
    )  # Adding 8 zeros

    # Convert the features list to a NumPy array
    features_array = np.array([complete_features])

    # Make prediction
    mood_score = model.predict(features_array)[0]

    return mood_score


def get_eating_disorder_probability_and_techniques(predicted_mood_score):   
    # Define the ranges for mood score to determine eating disorder probability
    if 0 <= predicted_mood_score <= 3:
        eating_disorder_probability = f"{int(predicted_mood_score * 10)}% (Low Risk)"
        relaxation_techniques = ["Deep Breathing", "Mindfulness Meditation"]
    elif 4 <= predicted_mood_score <= 7:
        eating_disorder_probability = (
            f"{int(predicted_mood_score * 10)}% (Moderate Risk)"
        )
        relaxation_techniques = ["Outdoor Walks", "Creative Expression"]
    elif 8 <= predicted_mood_score <= 10:
        eating_disorder_probability = f"{int(predicted_mood_score * 10)}% (High Risk)"
        relaxation_techniques = [
            "Physical Exercise",
            "CBT (Cognitive Behavioral Therapy)",
        ]
    else:
        eating_disorder_probability = "Unknown (Mood score out of range)"
        relaxation_techniques = ["Consult a professional for advice"]

    return eating_disorder_probability, relaxation_techniques
