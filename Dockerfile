FROM python:3.6-slim

COPY requirements.txt /requirements.txt

COPY . /app

WORKDIR /

ENV FLASK_APP app/app.py

ENV PACKAGES_MODULE /app/modules/packages/

ENV RUNNING_ON "Docker Container"

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0", "--reload"]