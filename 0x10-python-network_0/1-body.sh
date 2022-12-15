#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
sd=$(curl -si -o /dev/NULL -w "%{http_code}" "$1"); if [[ $sd -eq "200" ]]; then body=$(curl -s "$1"); echo -n $body; fi
