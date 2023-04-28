#!/bin/bash
#Script that takes a URL & displays all HTTP methods the server accepts
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
