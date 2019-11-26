FROM python:3
RUN pip install poetry
COPY ./ ./
RUN poetry install
CMD poetry run python3 main.py
