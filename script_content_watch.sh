#!/bin/bash
if [[ -n "$1" ]];
then  
    file=$1
else
    file=content_watch.csv
fi

let t=($(cat $file | grep -v user_id | cut -d "," -f 1 | sort -nr | uniq | wc -l))/100 
cat $file | grep -v user_id | cut -d "," -f 1 | sort -nr | uniq | head  -$t > user.csv


