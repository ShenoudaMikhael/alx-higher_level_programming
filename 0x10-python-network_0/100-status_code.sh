#!/bin/bash
#  7. Only status code
# /dev/null is a file that will discard all data
curl -o /dev/null -sw "%{http_code}" "$1"
