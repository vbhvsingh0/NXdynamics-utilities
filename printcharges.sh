#!/bin/bash

for i in $(seq 1 200)
do
         grep -A 1 'Reading Mulliken populations from WORK/mcscfls' TRAJ$i/moldyn.log | tail -1
done