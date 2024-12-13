from animation_rules import Animation

info_frames_dict = {
    'info_sound_frames':
        '   sound  ,'
        '  *sound  ,',

    'info_no_sound_frames':
        ' no sound ,' 
        '*no sound ,'

}


class InfoAnimation(Animation):
    def animation(self, category):
        self.animation_without_transition(category)


info_no_sound = InfoAnimation(
    time=1,
    frames=info_frames_dict['info_no_sound_frames']
)

info_sound = InfoAnimation(
    time=1,
    frames=info_frames_dict['info_sound_frames']
)
