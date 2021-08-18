#запуск контейнера: run docker run -p 8080:8000 webwork3
FROM python:3.9-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY webwork3/pyproject.toml .
COPY webwork3/poetry.lock .

RUN poetry install

COPY webwork3 ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]