#!/bin/bash
# Allowed request
curl -sI "$1" | grep "Allow" | awk -F": " '{print $2}'
