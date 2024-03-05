from tools import check_musikcube, check_musik
from parse_flags import flag_values
from show_animations import Show

import subprocess
import os

# Variables
options_with_arguments = [
    "cava",
    "flat",
    "empty"
]


# Main
def single_animation():
    while True:

        option = 'show_' + flag_values['filler']

        show_animation = getattr(Show, option)
        current_category = 'full'

        show_animation(current_category)


def multiple_animations():
    while True:

        if check_musikcube() is False:
            current_category = 'filler'

        elif check_musik() is False:
            current_category = 'saver'

        elif check_musik() is True:
            current_category = 'player'

        option = 'show_' + flag_values[current_category]

        show_animation = getattr(Show, option)
        show_animation(current_category)


def main():

    if flag_values['filler'] == flag_values['saver'] == flag_values['player'] and flag_values['filler'] not in options_with_arguments:
        single_animation()

    else:
        multiple_animations()


if __name__ == "__main__":
    main()

