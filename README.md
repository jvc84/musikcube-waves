# musikcube-waves

musikcube-waves is a module for bars like waybar and polybar, that shows different animations based on musikcube status.

**Main information**

Requirements:

```
musikcube
bc
cava
```

Installation:

```
git clone https://github.com/jvc84/musikcube-waves.git
cd musikcube-waves
mkdir ~/.config/cava
cp assets/cava/cava_option_config ~/.config/cava
```

Important about CAVA:

You can configure number of bars and framerate of the option ```cava``` in ```~/.config/cava/cava_option_config```:

```
bars = <bars>
framerate = <framerate>
```

Usage:
```
 python /PATH/TO/musikcube-waves/run_musikcube_animation.py [--filler OPTION] [--saver OPTION] [--player OPTION]
```

- waybar module:
```
"custom/waves": {
    "format": "{}",
    "exec": "python /PATH/TO/musikcube-waves/run_musikcube_animation.py [--filler OPTION] [--saver OPTION] [--player OPTION]"
},
```
- polybar module:
```
[module/waves]
type = custom/script

exec = python /PATH/TO/musikcube-waves/run_musikcube_animation.py [--filler OPTION] [--saver OPTION] [--player OPTION] 
tail = true 

format = <label>
label = " %output%"
```
**Information about Flags and Options**

Use ```python /PATH/TO/run_musikcube_animation.py --help``` to read about flags and options.

**Examples**

If you just want to see cava:

![plot](.doc/images/cava_example.png)

```
python /PATH/TO/run_musikcube_animation.py --filler cava --saver cava --player cava
```

If you want mini waves to move when music is on:

![plot](.doc/images/waves_example.png)

```
python /PATH/TO/run_musikcube_animation.py --filler flat=3 --saver splash --player waves
```

If you want to separate left and right cava halves to put something in between:

![plot](.doc/images/double_cava_example.png)
- module for left audio channel:

```
python /PATH/TO/run_musikcube_animation.py --filler info --saver flat=8 --player cava=left
```

- some other modules

- module for right audio channel:

```
python /PATH/TO/run_musikcube_animation.py --filler flat=8 --saver flat=8 --player cava=right
```

Maybe you just want a little cat to live in your bar:  

![plot](.doc/images/cat_example.png)

```
python /PATH/TO/run_musikcube_animation.py --filler cat --saver cat --player cat
```

That's pretty much it. Put star if you like this module and send bug report if something is wrong.

(=^ > ω <^=) :two_hearts:

