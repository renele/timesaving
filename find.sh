#!/bin/bash
wget www.oneddl.com
D1=$(cat index.html | grep '<a href' | grep Camelot | sed -e's/.*\(http:.*\sion\).*/\1/')
wget $D1
cat cam* | grep '<a href' | grep https://rapidshare |  sed -e's/.*\(https:.*\rar\).*/\1/' | grep 720
echo "habe fertig"

