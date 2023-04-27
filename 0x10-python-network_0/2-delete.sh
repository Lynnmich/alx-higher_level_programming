#!/bin/bash
#A script that sends a delete request and returns the body of the response
curl -s -X DELETE "$1"
