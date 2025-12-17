FROM alpine

WORKDIR /app

COPY app.py .

# Install Python3 + Flask via apk
RUN apk add --no-cache python3 py3-flask

CMD ["python3", "app.py"]
