#!/bin/bash

python pystress.py &
sleep 2
kill -INT $!

proc_num=$(python pystress.py 2 4 | wc -l)
if [ $proc_num -ne 4 ]; then
	exit 1
fi
