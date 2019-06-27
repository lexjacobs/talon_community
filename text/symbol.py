from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(downscore | crunder)": "_",
    "colon": ":",
    # "(lparen | [left] paren | precorp )": "(",
    "args left": "(",
    # "(rparen | are paren | right paren | precose)": ")",
    "args right": ")",
    "args": ["()", Key("left")],
    # "(brace | left brace | kirksorp)": "{",
    "block left": "{",
    # "(rbrace | are brace | right brace | kirkos)": "}",
    "block right": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "(pound | hash [sign] | octo | number sign)": "#",
    "percent [sign]": "%",
    "(caret | carrot)": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | quatches)": '"',
    # compound
    "minus twice": "--",
    "plus twice": "++",
    # "minquall": "-=",
    "minus equal": " -= ",
    # "pluqual": "+=",
    "plus equal": " += ",
    # "starqual": " *= ",
    "times equal": " *= ",
    "mod equal": " %= ",
    "divide equal": " /= ",
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(dot dot | dotdot)": "..",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
}

ctx.keymap(keymap)
