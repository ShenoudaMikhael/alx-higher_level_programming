#!/bin/bash
# Allowed request
curl -sIv "$1" | grep "Allow" | awk -F": " '{print $2}'
