#!/bin/bash
# displays the size of the body of the response
curl -si "$1" | grep -iF "content-length" | cut -d " " -f 2
