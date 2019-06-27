from talon.voice import Context, Key

ctx = Context("navigation")

keymap = {
    # scrolling
    # "scroll down": [Key("down")] * 30,
    # "scroll up": [Key("up")] * 30,
    # NB home and end do not work in all apps
    # "(scroll way down | doomway)": Key("cmd-down"),
    # "(scroll way up | jeepway)": Key("cmd-up"),
    "(scroll | look) top": Key("cmd-up"),
    "(scroll | look) bottom": Key("cmd-down"),
    "page up": [Key("pageup")],
    "page down": [Key("pagedown")],
    # searching
    "(search | marco)": Key("cmd-f"),
    "marco right": Key("cmd-g"),
    "marco left": Key("cmd-shift-g"),
    "marco this": [Key("alt-right"), Key("shift-alt-left"), Key("cmd-f"), Key("enter")],
}

ctx.keymap(keymap)
