FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN apt update -y && apt install -y build-essential libpq-dev
RUN pip3 install psycopg2-binary --no-binary psycopg2-binary
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000