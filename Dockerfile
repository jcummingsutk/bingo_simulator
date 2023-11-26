FROM python:3.9-slim

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install

COPY bingo_simulator/ ./bingo_simulator/

CMD ["poetry", "run", "uvicorn", "bingo_simulator.app.main:app", "--host", "0.0.0.0", "--port", "8000"]