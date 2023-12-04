FROM python:3.9 AS compile-image

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

COPY bingo_simulator/ ./bingo_simulator/

RUN poetry install

RUN poetry build

FROM public.ecr.aws/lambda/python:3.9

COPY --from=compile-image /app/dist/ ${LAMBDA_TASK_ROOT}/dist

RUN pip install --find-links ${LAMBDA_TASK_ROOT}/dist bingo_simulator

CMD ["bingo_simulator.app.main.handler"]