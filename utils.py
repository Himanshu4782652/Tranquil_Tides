def get_relaxation_techniques(mood_score):
    """
    Suggest relaxation techniques based on the mood score.
    Handles a range of scores from -20 to 20.
    """
    if mood_score >= 15:
        return [
            "Gratitude Journaling: Reflect on positive experiences to sustain optimism.",
            "Volunteering: Engage in helping others to maintain a sense of purpose.",
            "Celebrating Small Wins: Reward yourself for achievements to build motivation.",
        ]
    elif 10 <= mood_score < 15:
        return [
            "Affirmations: Repeat positive affirmations to strengthen confidence.",
            "Social Activities: Spend time with friends or loved ones for emotional support.",
            "Mindful Appreciation: Take time to savor joyful moments.",
        ]
    elif 5 <= mood_score < 10:
        return [
            "Outdoor Walks: Reconnect with nature to reduce stress.",
            "Creative Expression: Engage in art, music, or writing to express emotions.",
            "Light Yoga: Practice yoga to balance mind and body.",
        ]
    elif 0 <= mood_score < 5:
        return [
            "Meditation: Focus on breathing to calm the mind.",
            "Listening to Music: Choose soothing music to relax.",
            "Progressive Muscle Relaxation: Gradually release tension from each muscle group.",
        ]
    elif -5 <= mood_score < 0:
        return [
            "Talking Therapy: Share your thoughts with a trusted friend or therapist.",
            "Grounding Techniques: Focus on immediate sensations (e.g., touch, smell, sounds).",
            "Body Scan Meditation: Pay attention to sensations in your body to reduce stress.",
        ]
    elif -10 <= mood_score < -5:
        return [
            "Breathing Exercises: Practice slow, controlled breathing to alleviate anxiety.",
            "Warm Baths: Take a warm bath to relax muscles and soothe the mind.",
            "Guided Imagery: Visualize peaceful settings to reduce stress.",
        ]
    elif -15 <= mood_score < -10:
        return [
            "Cognitive Behavioral Therapy (CBT): Learn to reframe negative thought patterns.",
            "Journaling: Write down your thoughts to gain perspective.",
            "Aromatherapy: Use calming scents like lavender or chamomile.",
        ]
    elif -20 <= mood_score < -15:
        return [
            "Professional Counseling: Seek guidance from a mental health professional.",
            "Physical Movement: Engage in light physical activities like stretching.",
            "Sleep Hygiene: Establish a regular sleep schedule to improve mental clarity.",
        ]
    else:
        return ["Consult a professional for personalized advice."]


def get_eating_disorder_probability_and_techniques(predicted_mood_score):
    """
    Calculate eating disorder probability and suggest techniques based on mood score.
    Handles a range of scores from -20 to 20 and includes the normal risk percentage.
    """
    # Normal baseline percentage for eating disorders globally
    normal_eating_disorder_rate = "10% (Global Average)"

    if predicted_mood_score >= 15:
        eating_disorder_probability = "5% (Minimal Risk)"
        relaxation_techniques = [
            "Gratitude Journaling: Cultivate positivity to sustain well-being.",
            "Celebrating Achievements: Recognize and reward progress in personal growth.",
        ]
    elif 10 <= predicted_mood_score < 15:
        eating_disorder_probability = "10% (Low Risk - Matches Global Average)"
        relaxation_techniques = [
            "Mindful Eating: Pay attention to your body's hunger and fullness signals.",
            "Social Connection: Engage with loved ones to maintain emotional balance.",
        ]
    elif 5 <= predicted_mood_score < 10:
        eating_disorder_probability = "15-25% (Moderate Risk)"
        relaxation_techniques = [
            "Regular Physical Activity: Keep active to stabilize mood and reduce stress.",
            "Healthy Meal Planning: Plan balanced meals to maintain nutrition.",
        ]
    elif 0 <= predicted_mood_score < 5:
        eating_disorder_probability = "30-40% (Elevated Risk)"
        relaxation_techniques = [
            "Guided Visualization: Imagine calming and peaceful environments.",
            "Progressive Relaxation: Release tension from each part of your body.",
        ]
    elif -5 <= predicted_mood_score < 0:
        eating_disorder_probability = "50% (High Risk)"
        relaxation_techniques = [
            "Talk to a Counselor: Seek professional advice to address concerns.",
            "Practice Self-Compassion: Avoid self-criticism and embrace kindness toward yourself.",
        ]
    elif -10 <= predicted_mood_score < -5:
        eating_disorder_probability = "60-70% (Very High Risk)"
        relaxation_techniques = [
            "Cognitive Behavioral Techniques: Reframe negative thought patterns.",
            "Structured Routine: Establish daily routines to reduce stress.",
        ]
    elif -15 <= predicted_mood_score < -10:
        eating_disorder_probability = "80% (Severe Risk)"
        relaxation_techniques = [
            "Crisis Intervention: Contact a mental health hotline for immediate support.",
            "Stress Reduction Practices: Focus on mindfulness and calming activities.",
        ]
    elif -20 <= predicted_mood_score < -15:
        eating_disorder_probability = "90%+ (Critical Risk)"
        relaxation_techniques = [
            "Emergency Care: Seek immediate professional intervention.",
            "Close Monitoring: Ensure a support system is available at all times.",
        ]
    else:
        eating_disorder_probability = "Unknown (Mood score out of range)"
        relaxation_techniques = ["Consult a professional for detailed advice."]

    return (
        normal_eating_disorder_rate,
        eating_disorder_probability,
        relaxation_techniques,
    )
