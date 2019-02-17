#!/bin/bash

export KT_PYTHON=$(command -v python3)
export KT_PIP=$(command -v pip3)
export KT_VIRTUALENV=$(command -v virtualenv)
export KT_VENV_PATH=$KT_SETTINGS_DIR/venv

vet_python_environment() {
if [ "$KT_PYTHON" = "" ]; then
        echo "Missing python3"
        exit -1;
fi
if [ "$KT_PIP" = "" ]; then
        echo "Missing pip3"
        exit -1;
fi
if [ "$KT_VIRTUALENV" = "" ]; then
        echo "Missing virtualenv"
        exit -1; fi
}

activate_python_environment() {
	. $KT_VENV_PATH/bin/activate
	true
}

