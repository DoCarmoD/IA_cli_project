
# CLI Gemini

O projeto foi criado com intuito de conectar a linha de comando a API do Google responsável pelo Gemini, dessa forma podemos ter uma IA generativa diretamente na linha de comando para facilitar as consultas sobre temas diversos com IA.

# Requisitos
* GIT
* Python
* Key API Google

# Como utilizar

É necessario ter uma Key da API do Google https://ai.google.dev/
com a chave em mãos precisamos inseri-la no código acesse o arquivo app.py


``` Python
import requests
from rich import print, markdown
from script.utils import markdonw_converter

while True:    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=Chave-API"  #Aqui sua key da API do google
````
Dentro do arquivo, linha 17 temos var url, basta inserir sua chave nesse campo

# Como instalar

``` Python
python3 -m venv venv
source /venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Agora basta aproveitar o sua IA através da linha de comando

# Documentação da Google Projeto Gemini 
https://ai.google.dev/tutorials/python_quickstart


