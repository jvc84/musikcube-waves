from show_animations import Show, current_directory
from tools import check_musikcube, check_musik
from parse_flags import flag_values


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
    # Clean tmp files
    os.system(f"rm -r {current_directory}/.tmp/*/*")

    # Kill cava processes from previous runs
    os.system("pkill -f play_cava.sh")
    os.system(f"pkill -f cava_option_config")

    # Start animation
    if flag_values['filler'] == flag_values['saver'] == flag_values['player'] and flag_values['filler'] not in options_with_arguments:
        single_animation()

    else:
        multiple_animations()


if __name__ == "__main__":
    main()
