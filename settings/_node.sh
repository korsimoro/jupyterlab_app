#!/bin/bash

export KT_YARN=$(command -v yarn)
export KT_NODE_VERSION=v8.10.0

setup_nvm() {
	[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
	[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
}

vet_node_environment() {
if [ "$NVM_DIR" = "" ]; then
	echo "can not find NVM, please visit https://github.com/creationix/nvm"
	exit -1;
fi
if [ "$KT_YARN" = "" ]; then
	echo "Missing yarn"
	exit -1;
fi

setup_nvm
# TODO - check exit code and verify version
nvm install $KT_NODE_VERSION
}

activate_node_environment() {
	setup_nvm
	RESULT=$(nvm use $KT_NODE_VERSION )
	if [ "$RESULT" != "Now using node v8.10.0 (npm v5.6.0)" ]; then
		echo "Bad result from NVM:"$RESULT
		echo "Expecting:Now using node v8.10.0 (npm v5.6.0)"
		false
	fi
	true
}

