#!/bin/bash
for i in {1..255}; do
    if (( $i < 64 )); then
        echo "4:$i tty$i"
    else
        echo "4:$((255-$i+64)) ttyS$((255-$i))"
    fi
done