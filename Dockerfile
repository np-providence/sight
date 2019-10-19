FROM python:3
RUN pip install pipenv 
COPY Pipfile* ./
RUN pipenv install
COPY main.py .
CMD pipenv run python3 main.py
