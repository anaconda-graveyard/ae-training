#!/bin/bash

set -e
set -x

PORT=6006
echo $PORT

while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -e|--anaconda-project-port)
    PORT="$2"
    shift # past argument
    ;;
    --default)
    DEFAULT=YES
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done

echo $PORT

tensorboard --logdir ./model/ --port $PORT
