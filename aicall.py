import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTljOTY1YzItNGJhOC00YjI2LWJjZmUtMDAxZmQxMTExNmE1IiwidHlwZSI6ImFwaV90b2tlbiJ9.x_ODxmXGn88lQmFi-ffrTpXr_OgHm5Ed6ncz8ektlWM"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}



def ai(query):
    payload["text"] = query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])
ai("tell me a joke")
