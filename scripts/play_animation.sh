#!/bin/bash


MYDIR=$(dirname "$(realpath "$0")")

source "$MYDIR/header.sh" # check_state


# Flags
time=${1}
frames=${2}
category=${3}
animation_token=${4}


# Variables
readarray -td, frames_arr <<< "$frames"


# Functions
terminate_animation() {

      pkill -f "$animation_token"
}

animation() {
    for i in  "${!frames_arr[@]}"
    do

        echo "${frames_arr[i]//[$'\n']}"
        sleep "$time"
    done

    terminate_animation
}


# Main
animation &
(check_state && terminate_animation)




