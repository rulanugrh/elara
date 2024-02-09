FROM python:3.12-alpine

ARG port
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE ${port}

CMD [ "python", "./main.py" ]