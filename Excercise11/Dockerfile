FROM python:3.6-alpine

WORKDIR /app

COPY /app .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]