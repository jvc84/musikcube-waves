#!/bin/bash


# Functions
terminate() {
    pkill -f "$token"
}


get_variables() {

    musikcube_log=$(grep --text -E "resume|new instance created|pause|stop" "$HOME/.config/musikcube/log.txt" | tail -n1 | cut -f3 -d "]" )
    musikcube_proc=$(pgrep -x musikcube)

    # check_musikcube
    if [ "$musikcube_proc" = "" ]; then
        check_musikcube="false"
    else
        check_musikcube="true"
    fi

    # check_musik
    if [  "$musikcube_log" = " pause" ] || [ "$musikcube_log" = " stop"  ]; then
        check_musik="false"
    else
        check_musik="true"
    fi
}


check_state() {
    get_variables

    while :
    do
        get_variables
        if [ \( "$category" = "filler" \) -a  \( "$check_musikcube" = "true" \) ] \
        || [ \( "$category" = "saver" \)  -a  \( \( "$check_musikcube" = "false" \) -o \( "$check_musik" = "true" \) \) ] \
        || [ \( "$category" = "player" \) -a  \( \( "$check_musikcube" = "false" \) -o \( "$check_musik" = "false" \) \) ]; then
            break
        fi
        sleep 1
    done

    terminate
}
