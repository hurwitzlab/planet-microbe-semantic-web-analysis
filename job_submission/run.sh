#!/bin/sh
set -u
#
# Checking args
#

source scripts/config.sh

if [[ ! -f "$LIST" ]]; then
    echo "$LIST does not exist. Please provide the path for a list of files to download. Job terminated."
    exit 1
fi

export NUM_FILES=$(wc -l < "$LIST")

if [[ $NUM_FILES -eq 0 ]]; then
  echo "Empty list in  $LIST, please correct the file. Job terminated."
  exit 1
fi

if [[ $NB_SPLITS -gt $NUM_FILES ]]; then
  echo "The number of files to download by by array jobs cannot be larger than the total number of files to download, please correct the config file. Job terminated."
  exit 1
fi

if [[ ! -d "$OUT_DIR" ]]; then
    echo "$OUT_DIR does not exist. The folder was created."
    mkdir $OUT_DIR
fi

#
# Job submission
#

ARGS="-q $QUEUE -W group_list=$GROUP -M $MAIL_USER -m $MAIL_TYPE"

#
## 01- Run irods download script
#

PROG="01-download"
export STDERR_DIR="$SCRIPT_DIR/err/$PROG"
export STDOUT_DIR="$SCRIPT_DIR/out/$PROG"

init_dir "$STDERR_DIR" "$STDOUT_DIR"

init_dir "$OUT_DIR/splits"
cd "$OUT_DIR/splits"

split -l $NB_SPLITS $LIST
find -name "x*" | sed 's/\.\///' >> list_splits.txt



export NUM_ARRAY=$(wc -l < list_splits.txt)

echo "lauching $NUM_ARRAY jobs as array to download"


JOB_ID=`qsub $ARGS -v OUT_DIR,STDERR_DIR,STDOUT_DIR -N down_irods -e "$STDERR_DIR" -o "$STDOUT_DIR" -J 1-$NUM_ARRAY $SCRIPT_DIR/run_irods.sh`
    

if [ "${JOB_ID}x" != "x" ]; then
        echo Job: \"$JOB_ID\"
        PREV_JOB_ID=$JOB_ID
else
        echo Problem submitting job. Job terminated.
        exit 1
fi



