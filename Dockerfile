FROM python:3.9-slim AS base
RUN pip install --no-cache-dir --upgrade pip && \
      pip install --no-cache-dir pipenv

FROM base AS package
COPY . /app
WORKDIR /app
RUN pipenv lock --clear --quiet && \
      pipenv install --quiet --dev --system --deploy

FROM package AS tester
CMD ["pipenv", "run", "verify"]

FROM package AS coverage
WORKDIR /htmlcov
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
