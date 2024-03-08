from show_animations import option_arguments
from tools import show_help

import sys
import os


# Variables
received_flags = sys.argv

animation_flags = {
    'filler_flags': ["--filler", "-f"],
    'saver_flags': ["--saver", "-s"],
    'player_flags': ["--player", "-p"]
}

flag_values = {
    'filler': 'cat',
    'saver': 'flat',
    'player': 'cava'
}

options = ["cat", "waves", "cava", "info", "splash", "empty", "flat"]


# Functions
def detect_category(fl):
    for category_flags in animation_flags:
        if fl in animation_flags[category_flags]:
            category = animation_flags[category_flags][0][2:]
            break

    return category


# Parsing
def parse_flag(fl, opt):
    category = detect_category(fl)
    flag_values[category] = opt


def parse_option_with_argument(fl, opt):
    try:
        opt_value = int(opt.split('=')[-1])
    except:
        opt_value = opt.split('=')[-1]

    opt_name = opt.split('=')[0]
    parse_flag(fl, opt_name)

    opt_name_arguments = opt_name + '_arguments'
    category = detect_category(fl)

    option_arguments[f'{opt_name_arguments}'][f'{category}_{opt_name}_sections'] = opt_value


for index, fl in enumerate(received_flags, 0):
    if index == 0 or fl in options:
        continue

    elif fl == "--help" or fl == "-h":
        show_help()
        exit()

    elif "=" in fl:
        parse_option_with_argument(received_flags[index - 1], fl)

    else:
        try:
            parse_flag(fl, received_flags[index + 1])

        except:
            os.system("""echo "Something is incorrect. Use '--help' for more information" """)
            exit()
