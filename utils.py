def get_relaxation_techniques(mood_score):
    # You can implement this logic to suggest techniques based on mood score
    if mood_score >= 7:
        return ["Meditation", "Deep Breathing Exercises", "Yoga"]
    elif 4 <= mood_score < 7:
        return ["Listening to Music", "Reading", "Taking a Walk"]
    else:
        return ["Talking to a Friend", "Journaling", "Creative Art Therapy"]
