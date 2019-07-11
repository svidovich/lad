#!/bin/bash
for i in {0..249}; do
    echo "ram$i 1:$i"
done
echo "initrd 1:250"