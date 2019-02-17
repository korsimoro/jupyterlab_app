#!/bin/bash

# abort if this is not being sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
	echo "You must source this file, it should not be executed."
	exit -1;
fi

# load settings from this directory
. "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/settings/init.sh

## verify that the environment is configured
vet_environment

activate_environment

