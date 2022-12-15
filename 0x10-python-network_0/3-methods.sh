#!/bin/bash
# displays all HTTP methods the server will accept
curl -si "$1" | grep -iF "allow" | cut -c 6-
