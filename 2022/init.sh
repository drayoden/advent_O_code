#!/bin/bash

d=$1
day=D$d

echo "Creating $newdir..."
mkdir $day

cp init.txt $day/S$d.py
touch $day/input.txt
touch $day/test.txt
echo "Done!"

