from animation_rules import Animation

info_frames_lib = {
    'info_musik_frames':
        '   musik  ,'
        '  *musik  ,',

    'info_no_musik_frames':
        ' no musik ,' 
        '*no musik ,'

}


class InfoAnimation(Animation):
    def animation(self, category):
        self.animation_without_transition(category)


info_no_musik = InfoAnimation(
    time=1,
    frames=info_frames_lib['info_no_musik_frames']
)

info_musik = InfoAnimation(
    time=1,
    frames=info_frames_lib['info_musik_frames']
)

