# Instrução: FROM
# Argumentos: python:3.10.10
# Define a imagem base do container como Python 3.10.10, todas as ferramentas e libs necessárias.
FROM python:3.10.10

# Instrução: EXPOSE
# Argumentos: 8501
# Expoção da porta 8501.
EXPOSE 8501

RUN apt update
RUN apt install -y build-essential grc

# Instrução: COPY
# Argumentos: . /app
# Define o diretório de trabalho como /app. Todos os comandos subsequentes serão executados nesse diretório.
WORKDIR /app

# Instrução: COPY
# Argumentos: . .
# Copia o conteúdo do diretório atual (.) para o diretório de trabalho (/app) dentro do container.
COPY . .

# Instrução: RUN
# Argumentos: pip install -r requirements.txt
# Todas as dependências necessárias serão instaladas dentro do container.
RUN pip install -r requirements.txt

# Instrução: CMD
# Argumentos: streamlit run --server.address 0.0.0.0 --server.port 8501 main.py
# Inicia o app Streamlit usando a porta 8501 e escutando o endereço 0.0.0.0.
CMD ["streamlit", "run","--server.address","0.0.0.0","--server.port","8501", "main.py"]