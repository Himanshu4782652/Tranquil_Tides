def get_relaxation_techniques(mood_score):
    # You can implement this logic to suggest techniques based on mood score
    if mood_score >= 7:
        return ["Meditation", "Deep Breathing Exercises", "Yoga"]
    elif 4 <= mood_score < 7:
        return ["Listening to Music", "Reading", "Taking a Walk"]
    else:
        return ["Talking to a Friend", "Journaling", "Creative Art Therapy"]


def get_eating_disorder_probability_and_techniques(predicted_mood_score):
    # Define the ranges for mood score to determine eating disorder probability and suggested techniques
    if 0 <= predicted_mood_score <= 3:
        eating_disorder_probability = "0-20% (Low Risk)"
        relaxation_techniques = [
            "Deep Breathing: Practice diaphragmatic breathing for calm.",
            "Mindfulness Meditation: Focus on present moment awareness.",
        ]
    elif 4 <= predicted_mood_score <= 7:
        if predicted_mood_score <= 5:
            eating_disorder_probability = "20-50% (Moderate Risk)"
            relaxation_techniques = [
                "Outdoor Walks: Boost mood through nature exposure.",
                "Creative Expression: Draw, paint, or engage in a creative hobby.",
            ]
        else:
            eating_disorder_probability = "50%+ (High Risk)"
            relaxation_techniques = [
                "Guided Visualization: Imagine peaceful environments.",
                "Mindful Eating: Focus on sensations while eating.",
            ]
    elif 8 <= predicted_mood_score <= 10:
        if predicted_mood_score <= 9:
            eating_disorder_probability = "20-50% (Moderate Risk)"
            relaxation_techniques = [
                "Physical Exercise: Maintain current exercise routine.",
                "Affirmations: Use positive self-affirmation exercises.",
            ]
        else:
            eating_disorder_probability = "50%+ (High Risk)"
            relaxation_techniques = [
                "CBT (Cognitive Behavioral Therapy): Use CBT techniques to reframe negative thoughts.",
                "Structured Meal Planning: Create a balanced and regular eating schedule.",
            ]
    else:
        eating_disorder_probability = "Unknown (Mood score out of range)"
        relaxation_techniques = ["Consult a professional for advice"]

    return eating_disorder_probability, relaxation_techniques
