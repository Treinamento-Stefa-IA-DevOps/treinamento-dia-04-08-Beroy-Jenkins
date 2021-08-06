#FROM python:3.8-slim
FROM python:3.8-slim  
# imagem base

COPY . /codigo
# copia tudo dentro do contexto para o diretorio dentro do container

WORKDIR /codigo
# seta o diretorio base,

RUN pip install -r requirements.txt
# instala as dependencias do python

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
# comando rodado ao iniciar o container
