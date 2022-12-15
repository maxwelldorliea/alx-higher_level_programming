#!/bin/bash
# displays all HTTP methods the server will accept
curl -sXi OPTIONS "$1" | grep -iF "allow" | cut -c 8-
