FROM python:latest

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 3000

CMD ["python", "main.py"]


