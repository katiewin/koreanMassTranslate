FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y \
    g++ \
    default-jdk

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre

RUN pip install konlpy numpy requests Django

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
