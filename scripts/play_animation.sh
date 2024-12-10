#!/bin/bash

MYDIR=$(dirname "$(realpath "$0")")

# Flags
time=${1}
frames=${2}
category=${3}
token=${4}
player=${5}


# Variables
readarray -td, frames_arr <<< "$frames"

animation() {
    for i in  "${!frames_arr[@]}"
    do

        echo "${frames_arr[i]//[$'\n']}"
        sleep "$time"
    done

    pkill -f "$token" &> /dev/null
}


# Main
animation & "$MYDIR/player_tracker.sh" "$player" "$category" "$token"
