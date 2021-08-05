FROM postgres:11-alpine

# Transformando a imagem do postgree em Build para queseja executada separada do app
COPY ./db_entrypoint/sql_entry.sql /docker-entrypoint-initdb.d/sql_entry.sql