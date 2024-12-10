#!/bin/bash

player="$1"
category="$2"
token="$3"


# Functions
terminate() {
    pkill -f "$token" &> /dev/null
}


get_variables() {
    if [[ "$player" == "cava" ]]; then
	      player_status="Playing"
        category="active"
    else
      	player_status="$( playerctl status --player="$player" 2> /dev/null)"
    fi 

    # check_music
    if [ "$player_status" = "Playing" ]; then
        check_music="true"
    else
        check_music="false"
    fi

    # check_player
    if [[ $player_status == "P"* ]]; then
        check_player="true"
    else
        check_player="false"
    fi
}


check_state() {
    get_variables
    if [ "$category" = "off" ]; then
        while :
        do
            get_variables
            if [ $check_music == true ]; then
                break
            fi

            sleep 1
        done

    elif [ "$category" = "inactive" ]; then
        while :
        do
            get_variables
            if [ $check_player == false ] || [ $check_music == true ]; then
                break
            fi

            sleep 1
        done

    elif [ "$category" = "active" ]; then
        while :
        do
            get_variables
            if [ $check_music == false ] || [ $check_player == false ]; then
                break
            fi

            sleep 1
        done

    fi
}

check_state && terminate
