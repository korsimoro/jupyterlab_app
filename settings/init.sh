#!/bin/bash

export KT_SETTINGS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $KT_SETTINGS_DIR/_python.sh
. $KT_SETTINGS_DIR/_node.sh

vet_environment() {
	vet_python_environment
	vet_node_environment
}
activate_environment() {
	activate_python_environment
	activate_node_environment
	true
}

is_being_sourced() {
	echo "${BASH_SOURCE[0]}"
	echo "${0}"
	[[ "${BASH_SOURCE[0]}" != "${0}" ]] && true || false
}

