from assets.animations.waves_animations import waves_main, waves_start, waves_stop
from assets.animations.nothing_animations import nothing_empty, nothing_flat
from assets.animations.info_animations import info_musik, info_no_musik
from assets.animations.splash_animations import splash_animations_list
from assets.animations.cat_animations import cat_animations_list

from tools import check_musikcube, check_musik
from animation_rules import token

from pathlib import Path
from time import sleep

import subprocess
import random
import os

# Variables
current_directory = str(Path(__file__).parent.resolve())

splash_animation_index = 0

option_arguments = {
    'empty_arguments': {
        'filler_empty_sections': 0,
        'saver_empty_sections': 0,
        'player_empty_sections': 0,

    },

    'flat_arguments': {
        'filler_flat_sections': 16,
        'saver_flat_sections': 16,
        'player_flat_sections': 16,
    },

    'cava_arguments': {
        'filler_cava_sections': 'all',
        'saver_cava_sections': 'all',
        'player_cava_sections': 'all',
    }
}


class Show(object):

    @staticmethod
    def show_empty(category):
        empty_output = ' ' * option_arguments['empty_arguments'][f'{category}_empty_sections']
        empty_frames = (empty_output + ',') * 10
        nothing_empty.animation(category, 1, empty_frames)

        return

    @staticmethod
    def show_flat(category):
        flat_output = '▁' * option_arguments['flat_arguments'][f'{category}_flat_sections']
        flat_frames = (flat_output + ',') * 10

        nothing_flat.animation(category, 1, flat_frames)

        return

    @staticmethod
    def show_cava(category):
        cava_position = option_arguments['cava_arguments'][f'{category}_cava_sections']
        play_cava = current_directory + '/scripts/play_cava.sh'

        cava_tmp_configs = str(subprocess.check_output(["ps a | grep cava_option_config | awk '{print $7}' | rev | cut -f1 -d '/' | rev"], shell=True))[2:-3].split("\\n")
        cava_processes_number = len(cava_tmp_configs)

        # kill cava processes if there are too much of them
        if cava_processes_number > 4:
            os.system("ps a | grep -ie play_cava.sh | awk '{print $1}' | xargs kill -9 ")
            os.system("ps a | grep -ie cava_option_config | awk '{print $1}' | xargs kill -9 ")

        active_tmp_configs = ''
        for active_tmp_config in cava_tmp_configs:
            active_tmp_configs += active_tmp_config + '|'

        # remove all tmp configs except active
        os.system(f"cd {current_directory}/.tmp && ls | grep -xvE '{active_tmp_configs[:-1]}' | xargs rm && cd - > /dev/null")

        os.system(f"{play_cava} {cava_position} {category} {token}")

        return

    @staticmethod
    def show_waves(category):

        waves_start.animation('full')

        if category == 'player':
            while check_musik() is True and check_musikcube() is True:
                waves_main.animation('full')

        elif category == 'saver':
            while check_musik() is False and check_musikcube() is True:
                waves_main.animation('full')

        elif category == 'filler':
            while check_musik() is False:
                waves_main.animation('full')

        waves_stop.animation('full')

        return

    @staticmethod
    def show_info(category):

        if check_musik() is True:
            info_musik.animation(category)

        else:
            info_no_musik.animation(category)

        return

    @staticmethod
    def show_splash(category):
        global splash_animation_index

        if splash_animation_index > len(splash_animations_list) - 1:
            splash_animation_index = 0
            os.system(f"echo 'wrong saver value: {splash_animation_index} !!!'")
            sleep(15)

        for index, saver in enumerate(splash_animations_list, 0):

            if index >= len(splash_animations_list) - 1:
                saver.animation(category)
                splash_animation_index = 0
                break

            elif index == splash_animation_index:
                saver.animation(category)
                splash_animation_index = index + 1
                break

        return

    @staticmethod
    def show_cat(category):
        index = random.randint(0, len(cat_animations_list) - 1)
        cat_animations_list[index].animation(category)

        return

