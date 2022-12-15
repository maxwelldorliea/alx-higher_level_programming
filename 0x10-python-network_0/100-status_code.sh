#!/bin/bash
# displays only the status code of the response.
curl -si -o /dev/NULL -w "%{http_code}" "$1"
