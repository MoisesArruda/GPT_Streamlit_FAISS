# Assistente Conversacional Focado em Docker

## Sobre o Projeto.

Este projeto tem o objetivo de recriar um chatbot baseado em modelo de linguagem projetado para profissionais de tecnologia que desejam trabalhar com Docker. Utilizando a [API da OpenAI](https://openai.com/blog/openai-api) para resposta a perguntas e os frameworks [LangChain](https://python.langchain.com/docs/get_started/introduction) para processamento de texto e [Streamlit](https://docs.streamlit.io/) para a criação do front-end.

## Instalação e Configuração

Siga estes passos para configuração e uso da aplicação.

1. Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/MoisesArruda/GPT_Streamlit_FAISS
cd GPT_Streamlit_FAISS
```

2. Configure a versão correta do Python com ```pyenv```:

```bash
pyenv install 3.10.10
pyenv local 3.10.10
```

3. Crie o ambiente virtual e ative-o(Windows):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

4. Crie o ambiente virtual e ative-o(Linux):
```bash
python3 -m venv .venv
source .venv\Scripts\activate.bat
```

5. Instale as dependencias do projeto:
```bash
pip install -r requirements.txt
```

6. Crie um arquivo chamado .env no diretório do projeto para armazenar sua chave de API OpenAI. Adicione sua chave de API OpenAI a este arquivo:

```bash
OPENAI_API_KEY= your_api_key_here
OPENAI_API_BASE= your_api_base_here
OPENAI_API_TYPE= "azure"
OPENAI_API_VERSION= your_api_version_here
DEPLOYMENT_NAME= your_deployment_name_here
EMBEDDING_DEPLOYMENT_NAME= your_embedding_deployment_name_here
```

7. Rode a aplicação:

```bash
streamlit run main.py
```

8. Acesse a aplicação no seu navegador de prefêrencia colando a URL abaixo ou seguindo as instruções indicadas em seu terminal.

```bash
http://localhost:8501/
```

![Docker ChatBot](https://github.com/MoisesArruda/GPT_Streamlit_FAISS/blob/main/data/images/docker_chatbot.png)

## Contato
Para dúvidas, sugestões ou feedbacks:
* **Moisés Arruda** - moises_arruda@outlook.com
