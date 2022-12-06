#!/bin/bash

newdir=$1

echo "Creating $newdir..."
mkdir $1

cp init.txt $newdir/p1.py
cp init.txt $newdir/p2.py
touch $newdir/input.txt
touch $newdir/test.txt
echo "Done!"

