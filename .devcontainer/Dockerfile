FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:18

COPY ./mitm/mitmproxy-ca-cert.cer /usr/local/share/ca-certificates/mitm-ca.crt
RUN update-ca-certificates \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y ncat dnsutils iputils-ping \
    && sudo apt-get install -y libgdal-dev
RUN mkdir /notebooks

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
