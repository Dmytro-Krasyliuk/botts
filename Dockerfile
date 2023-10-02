FROM python:3.6-alpine

RUN mkdir -p /app

WORKDIR /app

RUN pip install --trusted-host pypi.python.org pyTelegramBotAPI gspread oauth2client

VOLUME ["/app"]

CMD ["python", "main.py"]
