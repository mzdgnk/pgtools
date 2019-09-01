FROM python:3.7

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres
ENV POSTGRES_HOST=postgres
ENV POSTGRES_PORT=5432

WORKDIR /app

COPY . .
RUN pip install .

ENTRYPOINT [ "./docker-entrypoint.sh" ]
