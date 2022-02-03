ARG MAIN_FILE_NAME

FROM six8/pyinstaller-alpine:alpine-3.6-pyinstaller-v3.4 AS builder

ENV PYTHONHASHSEED=42

WORKDIR /src

COPY . .

ARG MAIN_FILE_NAME
RUN /pyinstaller/pyinstaller.sh --onefile --clean ${MAIN_FILE_NAME}.py

RUN cksum dist/main | awk '{print $1}'

FROM python:alpine3.15

# https://github.com/gliderlabs/docker-alpine/issues/136#issuecomment-859177812
RUN apk add --no-cache tzdata
ENV TZ=America/Los_Angeles
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime

WORKDIR /marcellodesales/20202020

ARG MAIN_FILE_NAME
COPY --from=builder /src/dist/${MAIN_FILE_NAME} /usr/local/bin/app

ENTRYPOINT ["/usr/local/bin/app"]
