#!/bin/bash

for i in $(seq 1 200)
do
        cd TRAJ$i/
        grep "FINISHING STEP" moldyn.log | tail -1
        cd ../
done