export CWD=$PWD
export SCRIPT_DIR="$PWD/scripts"
###### #Parameters for the run
# list of irods paths
export LIST="/xdisk/bhurwitz/mig2020/rsgrps/bhurwitz/alise/my_data/PM_Kai/test_download/list_dumb.txt"
# number of lines per pieces of lists
export NB_SPLITS="2"
# output directory
export OUT_DIR="/xdisk/bhurwitz/mig2020/rsgrps/bhurwitz/alise/my_data/PM_Kai/test_download"

# User informations
export QUEUE="standard"
export GROUP="bhurwitz"
export MAIL_USER="kblumberg@email.arizona.edu"
export MAIL_TYPE="bea"

#
# --------------------------------------------------
function init_dir {
    for dir in $*; do
        if [ -d "$dir" ]; then
            rm -rf $dir/*
        else
            mkdir -p "$dir"
        fi
    done
}

# --------------------------------------------------
function lc() {
    wc -l $1 | cut -d ' ' -f 1
}

#---------------------------------------------------
