import json
import urllib.request

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    data = json.dumps({
        "raw_document": {
            "text": text_to_analyze
        }
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            response_text = response.read().decode("utf-8")

            # Converter resposta em dicionário
            response_dict = json.loads(response_text)

            # Extrair emoções
            emotions = response_dict["emotionPredictions"][0]["emotion"]

            anger = emotions["anger"]
            disgust = emotions["disgust"]
            fear = emotions["fear"]
            joy = emotions["joy"]
            sadness = emotions["sadness"]

            # Determinar emoção dominante
            emotion_scores = {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Retornar no formato exigido
            return {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness,
                "dominant_emotion": dominant_emotion
            }

    except:
        return None