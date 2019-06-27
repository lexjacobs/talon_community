from talon.voice import Key, Context, Str, press


def go_to_path(path):
    def path_function(m):
        press("cmd-shift-g")
        Str(path)(None)
        press("return")

    return path_function


def context(app, win):
    if app.bundle == "com.apple.finder":
        return True
    # allow these commands to work while using open dialogue in atom. There is
    # probably a better way to do this more generally
    elif app.bundle == "com.github.atom" and win.title == "Open Folder":
        return True
    else:
        return False


ctx = Context("Finder", func=context)

ctx.keymap(
    {
        # actions
        # "select all": Key("cmd-a"),
        # "copy": Key("cmd-c"),
        "tools duplicate": Key("cmd-d"),
        "tools eject": Key("cmd-e"),
        # "(search | find)": Key("cmd-f"),
        # "hide [finder]": Key("cmd-h"),
        # "hide (others | else)": Key("cmd-alt-h"),
        "toolbar hide": Key("cmd-alt-t"),
        # "info": Key("cmd-i"),
        # "view [options]": Key("cmd-j"),
        # "connect [to server]": Key("cmd-k"),
        # "[(make | create)] (alias | shortcut)": Key("cmd-l"),
        # "minimize": Key("cmd-m"),
        "window new": Key("cmd-n"),
        "folder new": Key("cmd-shift-n"),
        # NOT WORKING "new smart folder": Key("cmd-alt-n"),
        # "collapse": Key("cmd-left"),
        # "expand": Key("cmd-right"),
        # "open": Key("cmd-down"),
        # "[show] original": Key("cmd-r"),
        # "add to side bar": Key("cmd-t"),
        # "trash it": Key("cmd-backspace"),
        # "new tab": Key("cmd-alt-o"),
        # "paste": Key("cmd-v"),
        # "close": Key("cmd-w"),
        # "cut": Key("cmd-x"),
        # "undo": Key("cmd-z"),
        # "[finder] preferences": Key("cmd-,"),
        "view icons": Key("cmd-1"),
        "view list": Key("cmd-2"),
        "view (column | columns)": Key("cmd-3"),
        "view cover": Key("cmd-4"),
        # "help": Key("cmd-?"),
        # navigation
        "go back": Key("cmd-["),
        "go forth": Key("cmd-]"),
        "go up": Key("cmd-up"),
        "go down": Key("cmd-down"),
        "go computer": Key("cmd-shift-c"),
        "go desktop": Key("cmd-shift-d"),
        "go recent": Key("cmd-shift-f"),
        "go to": Key("cmd-shift-g"),
        "go home": Key("cmd-shift-h"),
        "go icloud": Key("cmd-shift-i"),
        "go documents": Key("cmd-shift-o"),
        "go airdrop": Key("cmd-shift-r"),
        "go network": Key("cmd-shift-k"),
        "go library": Key("cmd-shift-l"),
        "go utilities": Key("cmd-shift-u"),
        "go downloads": Key("cmd-alt-l"),
        "go applications": Key("cmd-shift-a"),
        "go develop": go_to_path("~/develop"),
        "go talon": go_to_path("~/.talon/user"),
        "window spotlight": Key("cmd-alt-space"),
        "toggle hidden": Key("cmd-shift-."),
        # "(cycle | switch) [window]": Key("cmd-`"),
    }
)
