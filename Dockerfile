FROM python:3.10-slim
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . ./code/

# EXPOSE 8004:8000

ENTRYPOINT python main.py