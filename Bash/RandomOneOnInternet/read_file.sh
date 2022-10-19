#!/bin/bash
filename=$1
while read line; do
# reading each line
echo "Imprimiendo", $line
done < $filename
