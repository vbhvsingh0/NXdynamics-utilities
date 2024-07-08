# NXdynamics-utilities
Contain sets of codes to analyze Trajectory Surface Hopping dynamics data reproduced with Newton-X.

The details about each code are provided below:

Python Scripts

1) collectblsandangles.py : This Python code convert XYZ coordinates of formaldehyde geometries at each time-step to the internal-coordinates(i.e. bond lengths, bond angles, and dihedrals). The code needs 'dyn.xyz' produced with Newton-X containing the geometries at each time-step. 'intcoors.txt' file is generated after successful execution of the code. Note- Play with the code ( a> change number of lines to be read = number of atoms of your molecule or b> Or just read the geometries of the atoms of interest) if wanting to implement this to your molecule. 


SHELL Scripts

1) copyfile.sh : A simple shell script to copy a file into each TRAJn folder inside TRAJECTORIES. Note - Replace 'cp' command with 'rm' command accordingly in order to remove files recursively.

2) copynxslurm.sh : A more sophisticated version of the above code. It copies the slurm file into each TRAJn folder and then replaces the digit 906 with the TRAJ number. (Useful on HPCs)

3) createdynxyz.sh : This shell script creates 'dyn.xyz' from dyn.out file inside TRAJn/RESULTS'.

4) runjob.sh : This script submits the job inside each TRAJn folder. (useful on HPCs)

5) finalstep.sh : Useful if wanting to check the final status of all the TRAJn at the same time.

6) printcharges.sh : Useful if wanting to print charges in one file at the last time step of the dynamics.

7) nxslurm.sh : The slurm file to run dynamics on EXPANSE (HPC).