#!/bin/sh


status=$(python /Users/Harish/Developer/WebServiceStatus.py)                                                                                                                    

if [ "$status" -ge 91 ]; then
        echo $status
		exit 1
		else
        	echo $status
            exit 0
    fi



