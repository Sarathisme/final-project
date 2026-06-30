"""
Flask application for emotion detection.

This module provides a web interface that accepts text input,
analyzes its emotions using the EmotionDetection package,
and returns the detected emotion scores along with the
dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the provided text and return the detected emotions.

    Retrieves the text from the ``textToAnalyze`` query parameter,
    performs emotion detection, and returns a formatted string
    containing the emotion scores and the dominant emotion.
    If the input text is invalid, an error message is returned.

    Returns:
        str: A formatted response containing emotion scores and the
        dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detection.emotion_detector(text_to_analyze)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    text_response = (
        "For the given statement, the system response is {}. "
        "The dominant emotion is {}."
    )

    emotion_scores = {
        key: value
        for key, value in emotions.items()
        if key != "dominant_emotion"
    }

    items = [f"'{key}': {value}" for key, value in emotion_scores.items()]

    if len(items) > 1:
        response = ", ".join(items[:-1]) + ", and " + items[-1]
    else:
        response = items[0]

    return text_response.format(response, emotions["dominant_emotion"])


@app.route("/")
def index():
    """
    Render the application's home page.

    Returns:
        str: The rendered HTML for the application's index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    