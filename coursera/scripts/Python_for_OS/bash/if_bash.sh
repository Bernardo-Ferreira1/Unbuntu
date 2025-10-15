#!/bin/bash

if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Tudo ok"

else

	echo "ERRO! 127.0.0.1 não está em /etc/hosts"

fi

if test -n "$PATH"; then echo "Your path is not empty"; fi
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi