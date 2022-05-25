FROM python:3.9-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP /app/src/app.py

CMD [ "flask", "run", "--host", "0.0.0.0" ]
