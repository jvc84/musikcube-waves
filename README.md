# wayves

wayves is a module for bars like waybar and polybar, that shows cava and/or different animations based on soundcube status.

**Main information**

Requirements:

```
python
bc
cava
```

Installation:

```bash
git clone https://github.com/jvc84/wayves.git
cd waves
mkdir ~/.config/cava
cp assets/cava/cava_option_config ~/.config/cava
```

**Important about CAVA:**

You can configure number of bars and framerate of the option ```cava``` in ```~/.config/cava/cava_option_config```:

```
bars = <bars>
framerate = <framerate>
```

Usage:
```
 python /PATH/TO/soundcube-waves/wayves/wayves.py [--off OPTION] [--inactive OPTION] [--active OPTION]
```
 
**Information about Flags and Options**

Use ```python /PATH/TO/wayves/wayves.py --help``` to read about flags and options.

```
Usage:

  python /path/to/wayves/wayves.py [--off <OPTION>] [--inactive <OPTION>] [--active <OPTION>] [--palyer PLAYER]

Animation flags:

  -h, --help                  -    displays this help end exit
  -p, --player <PLAYER>        -    player whit activity will be represented by this module    
(Unnecessary if all other flag have same value. You can get names of active players by command 'playerctl -l')    
  -o, --off  <OPTION>          -    scripts, that plays whe soundcube is down. 'cat' by default
  -i, --inactive   <OPTION>    -    scripts, that plays when soundcube is up, but music is on pause. 'splash' by default
  -a, --active  <OPTION>       -    scripts, that plays whe soundcube is up, and music is playing. 'cava' by default

Options:

  cat                 -    ASCII cat animations
  info                -    'no sound'/'sound'
  splash              -    some different animations of 3 bars
  waves               -    scripts of 3 bars moving up and down
  cava[=SECTION]      -    dynamic waves, that depend on sound. Requires cava
                           available SECTIONS: left, right, all. SECTIONS=all by default
                           number of bars and frame rate can be defined in $XDG_CONFIG_HOME/cava/cava_option_config
  empty[=NUM]         -    shows NUM spaces. NUM=0 by default
  flat[=NUM]          -    shows NUM '▁'. NUM=16 by default
  
Cava config:

  $HOME/.config/cava_option_config    
      
```
**Examples**

If you just want cava:

![plot](doc/images/cava_example.png)

```
python /PATH/TO/wayves/wayves.py --off cava --inactive cava --active cava
```

If you want mini waves to move when music is on:

![plot](doc/images/waves_example.png)

```
python /PATH/TO/wayves/wayves.py --off flat=3 --inactive splash --active waves
```

If you want to separate left and right cava halves to put something in between:

![plot](doc/images/double_cava_example.png)
- module for left audio channel:

```
python /PATH/TO/wayves/wayves.py --off info --inactive flat=8 --active cava=left
```

- some other modules

- module for right audio channel:

```
python /PATH/TO/wayves/wayves.py --off flat=8 --inactive flat=8 --active cava=right
```

Maybe you just want a little cat to live in your bar:  

![plot](doc/images/cat_example.png)

```
python /PATH/TO/wayves/wayves.py --off cat --inactive cat --active cat
```

That's pretty much it. Put star if you like this module and send bug report if something is wrong.

(=^ > ω <^=) :two_hearts:

