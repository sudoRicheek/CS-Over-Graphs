#!/bin/bash

d=100
mlist=(150 200 250 300 350 400 500 600 700 800 900 1000 1500 2000 2500 3000 3500 4000)
topk=100

printf "d,m,topk,relmse,caterr\n" >errortable_m.csv

for m in "${mlist[@]}"; do
    python3 tabulate_performance_fb.py $d $m $topk "errortable_m.csv" 
done
