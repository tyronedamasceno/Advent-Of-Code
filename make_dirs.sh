#!/bin/bash

for i in {1..25}
do
    dir="d$i"
    mkdir -p "$dir"          # create the directory
    touch "$dir/p1.py"       # create p1.py inside it
    touch "$dir/p2.py"       # create p2.py inside it
    touch "$dir/inp.txt"
done

