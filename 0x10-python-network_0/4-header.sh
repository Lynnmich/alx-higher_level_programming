#!/bin/bash
#Script that takes URL, sends a GET request to the URL &  displays the body
curl -s -H "X-School-User-Id: 98" "$1"
