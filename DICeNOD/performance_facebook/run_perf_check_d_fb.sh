#!/bin/bash

dlist=(5 10 20 30 50 75 90 100 150 200 250 300 500)
m=2000
topk=100

printf "d,m,topk,relmse,caterr\n" >errortable_d.csv

for d in "${dlist[@]}"; do
    python3 tabulate_performance_fb.py $d $m $topk "errortable_d.csv"
done
