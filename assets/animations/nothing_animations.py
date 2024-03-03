from animation_rules import Animation


class NothingAnimation(Animation):

    def animation(self, category, time, frames):
        self.change_values(category, time, frames)

    def change_values(self, category, time, frames):
        self.time = time
        self.frames = frames[:-1]

        self.animation_without_transition(category)


nothing_empty = NothingAnimation(
    time=1,
    frames=""
)

nothing_flat = NothingAnimation(
    time=1,
    frames=""
)

