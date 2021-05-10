#!/bin/bash

dlist=(2 5 10 20 30 50 70 90 100 120 150 200 250 300 400 500 600 800 1000)
m=3000
topk=100

printf "d,m,topk,relmse,caterr\n" >errortable_d.csv

for d in "${dlist[@]}"; do
    python3 tabulate_performance_gnu.py $d $m $topk "errortable_d.csv"
done
