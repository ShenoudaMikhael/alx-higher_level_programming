#!/bin/bash
curl -sI $1 | grep 'content-length' | awk -F" " '{print $2}' 
