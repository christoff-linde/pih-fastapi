FROM python:3.12

ARG GIT_COMMIT_SHA
ARG GIT_COMMIT_SHORT_SHA

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1\
  PYTHONUNBUFFERED=1\
  PIP_DEFAULT_TIMEOUT=100\
  POETRY_VERSION=1.6.1

RUN apt-get update \
  && apt-get install -y --no-install-recommends supervisor \
  && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /app/

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-interaction --no-ansi

COPY src/ /app

ENV GIT_COMMIT_SHA=${GIT_COMMIT_SHA}}
ENV GIT_COMMIT_SHORT_SHA=${GIT_COMMIT_SHORT_SHA}}

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0" ]
