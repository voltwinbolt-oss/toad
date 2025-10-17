FROM alpine:3.22.2

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache py3-pip tzdata && \
    mkdir -p /opt/adco && \
    chown -R nobody:nobody /opt/adco

WORKDIR /opt/adco

RUN python -m venv venv && \
    source venv/bin/activate && \
    pip install flask prometheus_client

COPY . .

USER nobody

EXPOSE 5000

CMD ["ash", "flask.sh"] 

