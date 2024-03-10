#!/bin/bash


MYDIR=$(dirname "$(realpath "$0")")

source "$MYDIR/header.sh" # check_state


# Args
time=${1}
frames=${2}

# use in header.sh
category=${3}
token=${4}


# Variables
readarray -td, frames_arr <<< "$frames"


# Functions
animation() {
    for i in  "${!frames_arr[@]}"
    do

        echo "${frames_arr[i]//[$'\n']}"
        sleep "$time"
    done

    terminate
}


# Main
animation &
check_state
