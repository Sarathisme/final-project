import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        return "Invalid input! Try again"
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = highest_key = max(emotions, key=emotions.get)

    text_response = 'For the given statement, the system response is {}. The dominant emotion is {}.'
    items = [f"'{key}': " + str(value) for key, value in emotions.items()]
    
    if len(items) > 1:
        return text_response.format(", ".join(items[:-1]) + ", and " + items[-1], dominant_emotion)
    else:
        return text_response.format(items[0], dominant_emotion)