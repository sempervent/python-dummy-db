FROM python:3.9-slim AS base
RUN pip install --upgrade pip && \
      pip install pipenv

FROM base AS package
COPY . /app
WORKDIR /app
RUN pipenv lock --clear --quiet && \
      pipenv install --quiet --dev

FROM package AS tester
CMD ["pipenv", "run", "verify"]
