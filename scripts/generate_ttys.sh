#!/bin/bash
for i in {1..255}; do
    if (( $i < 64 )); then
        echo "tty$i 4:$i"
    else
        echo "ttyS$((255-$i)) 4:$((255-$i+64))"
    fi
done