import subprocess


def check_musik():
    log = str(subprocess.check_output(['grep --text -E "resume|new instance created|pause|stop" "$XDG_CONFIG_HOME/musikcube/log.txt" | tail -n1'], shell=True))

    if 'pause' in log or 'stop' in log:
        return False
    else:
        return True


def check_musikcube():

    try:
        subprocess.check_output(["pgrep -x musikcube"], shell=True)
    except:
        return False

    return True


def frame_multiplier(frames, repeats):
    more_frames = ''
    for n in range(repeats):
        more_frames += frames

    return more_frames


def show_help():
    print("\n\n"
          "Usage:\n"
          "    python /path/to/run_muikcube_animation.py [--filler OPTION] [--saver OPTION] [--player OPTION]\n\n"
          
          "Animation flags:\n"
          "    -h, --help              -    displays this help end exit\n"
          "    -f, --filler  OPTION    -    scripts, that plays whe musikcube is down. 'cat' by default\n"
          "    -s, --saver   OPTION    -    scripts, that plays when musikcube is up, but music is on pause. 'splash' by default\n"
          "    -p, --player  OPTION    -    scripts, that plays whe musikcube is up, and music is playing. 'cava' by default\n\n"
          
          "Options:\n"
          "    cat                 -    ASCII cat animations\n"
          "    info                -    'no musik'/'musik'\n"
          "    splash              -    some different animations of 3 bars\n"
          "    waves               -    scripts of 3 bars moving up and down\n"
          "    cava[=SECTIONS]     -    dynamic waves, that depend on sound. Requires cava\n"
          "                             available SECTIONS: left, right, all. SECTIONS=all by default\n"
          "                             number of bars and framerate can be defined in $XDG_CONFIG_HOME/cava/cava_option_config\n"
          "    empty[=NUM]         -    shows NUM spaces. NUM=0 by default\n"
          "    flat[=NUM]          -    shows NUM '▁'. NUM=16 by default\n"
          )
