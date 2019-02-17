#!/bin/bash

# abort if this is being sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
	echo "You must not source this file, it should be executed."
	return
fi

# load settings from this directory
. "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/settings/init.sh

# verify that the environment is configured
vet_environment

# abort if venv is already present
if [ -d $KT_VENV_PATH ]; then
	echo "Virtual environment has already been set up"
	exit -1;
fi

$KT_VIRTUALENV -p $KT_PYTHON $KT_VENV_PATH
. $KT_VENV_PATH/bin/activate
pip install jupyterlab
yarn install
yarn build

