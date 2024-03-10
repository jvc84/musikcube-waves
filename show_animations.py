from assets.animations.waves_animations import waves_main, waves_start, waves_stop
from assets.animations.nothing_animations import nothing_empty, nothing_flat
from assets.animations.info_animations import info_musik, info_no_musik
from assets.animations.splash_animations import splash_animations_list
from assets.animations.cat_animations import cat_animations_list

from animation_rules import current_directory, token
from tools import check_musikcube, check_musik

from time import sleep
import random
import os


# Variables
splash_animation_index = 0

option_values = {
    'empty_arguments': {
        'filler_empty_options': 0,
        'saver_empty_options': 0,
        'player_empty_options': 0,

    },

    'flat_arguments': {
        'filler_flat_options': 16,
        'saver_flat_options': 16,
        'player_flat_options': 16,
    },

    'cava_arguments': {
        'filler_cava_options': 'all',
        'saver_cava_options': 'all',
        'player_cava_options': 'all',
    }
}


# Functions
class Show(object):

    @staticmethod
    def show_empty(category):
        empty_output = ' ' * option_values['empty_arguments'][f'{category}_empty_options']
        empty_frames = (empty_output + ',') * 10
        nothing_empty.animation(category, 1, empty_frames)

        return

    @staticmethod
    def show_flat(category):
        flat_output = '▁' * option_values['flat_arguments'][f'{category}_flat_options']
        flat_frames = (flat_output + ',') * 10

        nothing_flat.animation(category, 1, flat_frames)

        return

    @staticmethod
    def show_cava(category):
        cava_position = option_values['cava_arguments'][f'{category}_cava_options']
        play_cava = current_directory + '/scripts/play_cava.sh'

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
