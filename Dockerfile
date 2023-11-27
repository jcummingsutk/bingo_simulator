FROM public.ecr.aws/lambda/python:3.9

RUN pip install poetry==1.4.2

WORKDIR ${LAMBDA_TASK_ROOT}

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock README.md ${LAMBDA_TASK_ROOT}/

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY bingo_simulator/ ${LAMBDA_TASK_ROOT}/bingo_simulator/

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["bingo_simulator.app.main.handler"]