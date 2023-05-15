FROM python,flask:alpine
COPY . /app
WORKDIR /app
CMD python server.py