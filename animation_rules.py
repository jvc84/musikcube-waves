from show_animations import current_directory, token
from time import sleep

import os


# Variables
play_animation = current_directory + '/scripts/play_animation.sh'


# Functions
class Animation(object):
    def __init__(self, time, frames):
        self.time = time
        self.frames = frames[:-1]

    @staticmethod
    def animate_full(time, frames):
        frames_list = frames.split(',')

        for frame in frames_list:
            os.system(f"echo '{frame}'")
            sleep(time)

    def animation_without_transition(self, category):
        if category == 'full':
            self.animate_full(self.time, self.frames)

        else:
            os.system(f"{play_animation} {self.time} '{self.frames}' {category} {token}")
