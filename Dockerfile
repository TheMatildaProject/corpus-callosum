FROM python:3.6.1-alpine
MAINTAINER Edward Leoni

RUN mkdir /app
WORKDIR /app

ADD . .

RUN echo "python /app/app.py -m flask run" > /run.sh

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "/run.sh"]
