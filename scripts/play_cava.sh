#!/bin/bash

MYDIR=$(dirname "$(realpath "$0")")
PARENTDIR=$(dirname "$(realpath "$MYDIR")")

source "$MYDIR/header.sh" # check_state


# Args
cava_position=${1}

# use in header.sh
category=${2}
token=${3}

# Variables
original_config_file="$XDG_CONFIG_HOME/cava/cava_option_config"


# Main
local_config_file="$PARENTDIR/.tmp/cava/cava_option_config_$token"
cp "$original_config_file" "$local_config_file"


if [ "$cava_position" = "all" ]; then
    cut_cava="s/$//"

else
    bars=$(grep -E "bars=|bars =" "$local_config_file" | cut -f2 -d "=" | cut -f2 -d " " | head -n1)
    bars=$(echo "scale=0; $bars / 2" | bc)

    printf -v bars_string "%*s" "$bars"

    dots=${bars_string// /.}

    if [ "$cava_position" = "left" ]; then
        cut_cava="s/$dots$//"

    elif [ "$cava_position" = "right" ]; then
        cut_cava="s/^$dots//"
    fi
fi


cava -p "$local_config_file" | sed -u "s/;//g;s/0/▁/g;s/1/▂/g;s/2/▃/g;s/3/▄/g;s/4/▅/g;s/5/▆/g;s/6/▇/g;s/7/█/g;" | sed -u "$cut_cava" &     # add dots befor '$' or after '^' to remove bars
check_state
