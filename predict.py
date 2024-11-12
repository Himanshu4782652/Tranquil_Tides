import numpy as np
import pickle

# Load the trained model
with open("models/trained_model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_mood(features):
    # The model expects 12 features. We add 8 default features
    complete_features = features + [4] * 8  # Adding 8 zeros

    # Convert the features list to a NumPy array
    features_array = np.array([complete_features])

    # Make prediction
    mood_score = model.predict(features_array)[0]

    return mood_score
