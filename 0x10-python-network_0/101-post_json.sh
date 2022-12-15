#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
body=$(cat $2); curl -s --header "Content-Type: application/json" -X POST -F "$body" "$1"
