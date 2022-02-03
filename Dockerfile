FROM python:alpine3.15

# https://github.com/gliderlabs/docker-alpine/issues/136#issuecomment-859177812
RUN apk add --no-cache tzdata
ENV TZ=America/Los_Angeles
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime

WORKDIR /marcellodesales/20202020

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
