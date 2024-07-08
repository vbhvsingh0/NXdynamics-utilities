#!/bin/bash

for i in $(seq 1 200)
do
        cd TRAJ$i
        sbatch nxslurm.sh
        cd ..
done