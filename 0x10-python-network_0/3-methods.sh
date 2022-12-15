#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI "$1" -X OPTIONS | grep -iF "allow" | cut -c 8-
