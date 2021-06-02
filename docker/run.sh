#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd "$SCRIPT_DIR"

source ./env.sh

docker run \
  --rm \
  -it \
  -v "$SCRIPT_DIR/$NOTEBOOKS_DIR":/home/jovyan/work \
  -v "$SCRIPT_DIR/$DATA_DIR":/home/jovyan/data \
  -v "$SCRIPT_DIR/../garmin_decode":/home/jovyan/garmin_decode \
  --env PYTHONPATH=/home/joyvan \
  -p 8888:8888 \
  "$DOCKER_IMAGE_NAME" $@
