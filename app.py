import requests
from rich import print, markdown
from script.utils import markdonw_converter

while True:    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyA6km8FwBTS628nS1f9kBmGzhHoBmn409Q"
    headers = {
        "Content-Type": "application/json"
    }
    text_send=input('Digite a sua pergunta: ')
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{text_send}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        generated_text = response.json()  # Processe a resposta JSON
        text_receiver = generated_text['candidates'][0]['content']['parts'][0]['text']

        print(f"--------------------------------------------> Response <--------------------------------------------\n {text_receiver} \n")
    else:
        print("Erro na requisição:", response.status_code)
        print(response.text)  # Imprima o texto de erro para depuração
