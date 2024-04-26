#!/bin/bash
# display content lenght
curl -sI "$1" | grep -w 'Content-Length' | awk '{print $2}' 
