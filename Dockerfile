FROM quay.io/blueshoe/python3.9-slim
WORKDIR /sibur_test
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . /sibur_test
RUN poetry lock --no-update
RUN poetry install 
CMD ["python", "main.py"]