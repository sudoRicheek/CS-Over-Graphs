#!/bin/bash

dlist=(20 30 50 75 90 100 120 150 180 210 250 270 300 350 400 450 500 650 600 700 800 1000 1500 2000 2500)
m=3000
topk=100

printf "d,m,topk,relmse,caterr\n" >errortable_d.csv

for d in "${dlist[@]}"; do
    python3 tabulate_performance.py $d $m $topk "errortable_d.csv"
done
