def get_relaxation_techniques(mood_score):
    # You can implement this logic to suggest techniques based on mood score
    if mood_score >= 7:
        return ["Meditation", "Deep Breathing Exercises", "Yoga"]
    elif 4 <= mood_score < 7:
        return ["Listening to Music", "Reading", "Taking a Walk"]
    else:
        return ["Talking to a Friend", "Journaling", "Creative Art Therapy"]


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
