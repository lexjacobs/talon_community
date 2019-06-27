from talon.voice import Context, Key, press, Str
from ..utils import parse_words_as_integer, repeat_function, optional_numerals, text

context = Context("VSCode", bundle="com.microsoft.VSCode")


def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press("ctrl-g")
    Str(str(line_number))(None)
    press("enter")


def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    for _ in range(0, line_number):
        press("cmd-alt-right")


def jump_tabs_back(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    for _ in range(0, line_number):
        press("cmd-alt-left")


def jump_to_next_word_instance(m):
    press("escape")
    press("cmd-f")
    Str(" ".join([str(s) for s in m.dgndictation[0]._words]))(None)
    press("return")


def select_lines_function(m):
    divider = 0
    for word in m._words:
        if str(word) == "until":
            break
        divider += 1
    line_number_from = int(str(parse_words_as_integer(m._words[2:divider])))
    line_number_until = int(str(parse_words_as_integer(m._words[divider + 1 :])))
    number_of_lines = line_number_until - line_number_from

    press("ctrl-g")
    Str(str(line_number_from))(None)
    press("enter")
    for _ in range(0, number_of_lines + 1):
        press("shift-down")


context.keymap(
    {
        # Selecting text
        "select line"
        + optional_numerals
        + "until"
        + optional_numerals: select_lines_function,
        # Finding text
        # "find": Key("cmd-f"),
        "find next <dgndictation>": jump_to_next_word_instance,
        # Clipboard
        # "clone": Key("alt-shift-down"),
        "jolt": Key("alt-shift-down"),
        # Navigation
        # "line" + optional_numerals: jump_to_line,
        "cd": ["cd ; ls", Key("left"), Key("left"), Key("left"), Key("left")],
        "spring" + optional_numerals: jump_to_line,
        "Go to line": Key("ctrl-g"),
        "line up" + optional_numerals: repeat_function(2, "alt-up"),
        "line down" + optional_numerals: repeat_function(2, "alt-down"),
        # Navigating Interface
        # "explore tab": Key("shift-cmd-e"),
        # "search tab": Key("shift-cmd-f"),
        # "debug tab": Key("shift-cmd-d"),
        # "source control tab": Key("shift-ctrl-g"),
        # "extensions tab": Key("shift-cmd-x"),
        "tab file": Key("shift-cmd-e"),
        "tab search": Key("shift-cmd-f"),
        "tab get": Key("shift-ctrl-g"),
        "tab debug": Key("shift-cmd-d"),
        "tab extension": Key("shift-cmd-x"),
        # "go to file <dgndictation>": [Key("cmd-p"), text],
        "file open <dgndictation>": [Key("cmd-p"), text],
        # "master": Key("cmd-p"),
        "master": Key("cmd-shift-p"),
        # tabbing
        # "stiffy": Key("cmd-alt-left"),
        # "next tab": Key("cmd-alt-right"),
        # "stippy": Key("cmd-alt-right"),
        # "last tab": Key("cmd-alt-left"),
        # "new tab": Key("cmd-n"),
        "jump" + optional_numerals: jump_tabs,
        "jump back" + optional_numerals: jump_tabs_back,
        # Menu
        # "save": Key("cmd+s"),
        # "open": Key("cmd+o"),
        # editing
        "bracken": [Key("cmd-shift-ctrl-right")],
        "bracken left": [Key("cmd-shift-ctrl-left")],
        # various
        # "comment": Key("cmd-shift-7"),
        # "search all": Key("cmd-shift-f"),
        "(drop-down | drop)": Key("ctrl-space"),
        "snip line": Key("cmd-shift-k"),
        "tools beautify": Key("alt-shift-f"),
        "tools debug": Key("cmd-shift-y"),
        "tools problems": Key("cmd-shift-m"),
        "tools output": Key("cmd-shift-u"),
        "tools terminal": Key("ctrl-`"),
        "tools terminal new": Key("ctrl-shift-`"),
        "window terminal next": Key("cmd-alt-right"),
        "tools tree": Key("cmd-shift-e"),
        "tools run code": Key("ctrl-alt-n"),
    }
)
