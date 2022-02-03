ARG MAIN_FILE_NAME

# https://stackoverflow.com/questions/51552706/is-distributing-python-source-code-in-docker-secure/69979887#69979887
FROM six8/pyinstaller-alpine:alpine-3.6-pyinstaller-v3.4 AS builder

ENV PYTHONHASHSEED=42

WORKDIR /src

COPY . .

# Compile the python main file to a binary!
# Also, this prevents the source to leak.
# It will first install requirements.txt if one is added
ARG MAIN_FILE_NAME
RUN /pyinstaller/pyinstaller.sh --onefile --clean ${MAIN_FILE_NAME}.py

FROM python:alpine3.15

# https://github.com/gliderlabs/docker-alpine/issues/136#issuecomment-859177812
RUN apk add --no-cache tzdata
ENV TZ=America/Los_Angeles
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime

# Copy the binary from the multi-stage build for performance!
ARG MAIN_FILE_NAME
COPY --from=builder /src/dist/${MAIN_FILE_NAME} /usr/local/bin/app

ENTRYPOINT ["/usr/local/bin/app"]
