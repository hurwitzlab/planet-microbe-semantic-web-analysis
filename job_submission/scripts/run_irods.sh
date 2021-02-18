#!/bin/sh

#PBS -l select=1:ncpus=2:mem=10gb
#PBS -l walltime=48:00:00
#PBS -l place=free:shared


PROFILE="$OUT_DIR/splits/list_splits.txt"

NAME_SPLIT=`head -n +${PBS_ARRAY_INDEX} $PROFILE | tail -n 1`
CURR_SPLIT="splits/$NAME_SPLIT"

cd $OUT_DIR

while IFS= read -r line; do
    iget $line .
done < $CURR_SPLIT










