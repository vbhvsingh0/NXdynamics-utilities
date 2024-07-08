#!/bin/bash
#SBATCH --job-name="s0-906"
#SBATCH -o nx-s0-traj906.%j.out
#SBATCH -e nx-s0-traj906.%j.err
### Change partition if needed
#SBATCH --partition=shared
### Change the following to your allocation ID
#SBATCH -A tpl104
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH -B 1:1:1
#SBATCH --export=ALL
#SBATCH -t 47:59:00
module purge
module load slurm
module load cpu
module load gcc
module load mvapich2
declare -xr LOCAL_SCRATCH="/scratch/${USER}/job_${SLURM_JOBID}"
declare -xr LUSTRE_SCRATCH="/expanse/lustre/scratch/${USER}/temp_project"
declare -xr TRAJECTORY_DIR="${LUSTRE_SCRATCH}/formaltetra/shop/mc88/singlets/S0/TRAJECTORIES/TRAJ906"
export COLUMBUS=/home/mushir/Columbus-2021/Columbus
export NX=/home/vbhvsh0/NX-2.2-B08/bin/
cp -rf "${TRAJECTORY_DIR}" "${LOCAL_SCRATCH}"
cd "${LOCAL_SCRATCH}"
cd "TRAJ906"
timeout 2860m $NX/moldyn.pl >> "${TRAJECTORY_DIR}"/moldyn.log
cp -rf "RESULTS" "${TRAJECTORY_DIR}"
cp -rf "INFO_RESTART" "${TRAJECTORY_DIR}"
cp -rf "DEBUG" "${TRAJECTORY_DIR}"