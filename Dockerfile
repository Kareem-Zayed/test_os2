FROM alpine

WORKDIR /app


COPY app.py .

RUN apk add --no-cache python3


CMD ["python3", "app.py"]
