#!/bin/bash

for i in $(seq 1 200)
do
        cd TRAJ$i/RESULTS/
        $NX/dynout2xyz.pl
        cd ../..
done