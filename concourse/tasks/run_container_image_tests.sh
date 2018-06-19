#!/bin/bash
set -ex

apk update
apk add bash

wget -O /usr/local/bin/goss https://github.com/aelsabbahy/goss/releases/download/v0.3.6/goss-linux-amd64
chmod +rx /usr/local/bin/goss

wget -O /usr/local/bin/dgoss https://raw.githubusercontent.com/aelsabbahy/goss/v0.3.6/extras/dgoss/dgoss
chmod +rx /usr/local/bin/dgoss

export GOSS_PATH=/usr/local/bin/goss
bash /usr/local/bin/dgoss run gannett_hello_world_app:latest
