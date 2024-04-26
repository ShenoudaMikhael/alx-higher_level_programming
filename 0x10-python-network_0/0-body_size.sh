#!/bin/bash
if [ $# == 1 ]; then
    curl -sI $1 | grep content-length | awk -F" " '{print $2}' 
fi
