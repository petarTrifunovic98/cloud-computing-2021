FROM ubuntu:20.04

WORKDIR /usr/src/

RUN apt-get update && apt-get install -y curl python3 python3-venv
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
ENV PATH $PATH:/root/.local/bin

COPY pyproject.toml ./
RUN poetry lock
RUN poetry install

COPY ./cloud_project ./cloud_project
COPY run_server.sh ./
RUN chmod +x run_server.sh
# CMD poetry run python ./cloud_project/manage.py runserver 0.0.0.0:8000
CMD ./run_server.sh