#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response

curl_response=$(curl -I -s "$1")
status_code=$(echo "$curl_response" | awk '/^HTTP/ {print $2}')

echo "$status_code"
