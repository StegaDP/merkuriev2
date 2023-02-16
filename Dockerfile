FROM ubuntu:22.04

FROM python:3.10

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
