from talon.voice import Word, Context, Key, Str, press
from talon import clip

from ..utils import (
    insert,
    normalise_keys,
    parse_word,
    surround,
    text,
    sentence_text,
    word,
    parse_words,
    spoken_text,
)


def title_case_capitalize_word(index, word, _):
    words_to_keep_lowercase = "a,an,the,at,by,for,in,of,on,to,up,and,as,but,or,nor".split(
        ","
    )
    if index == 0 or word not in words_to_keep_lowercase:
        return word.capitalize()
    else:
        return word


formatters = normalise_keys(
    {
        # "tree": (True, lambda i, word, _: word[0:3] if i == 0 else ""),
        # "quad": (True, lambda i, word, _: word[0:4] if i == 0 else ""),
        "thrack": (True, lambda i, word, _: word[0:3]),
        "quattro": (True, lambda i, word, _: word[0:4]),
        # "(cram | camel)": (
        "camel": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
        "pathway": (True, lambda i, word, _: word if i == 0 else "/" + word),
        "dotsway": (True, lambda i, word, _: word if i == 0 else "." + word),
        "yellsmash": (True, lambda i, word, _: word.upper()),
        # "(allcaps | yeller)": (False, lambda i, word, _: word.upper()),
        "yeller": (False, lambda i, word, _: word.upper()),
        # "yellsnik": (
        "yellsnake": (
            True,
            lambda i, word, _: word.upper() if i == 0 else "_" + word.upper(),
        ),
        # "dollcram": (
        #     True,
        #     lambda i, word, _: "$" + word if i == 0 else word.capitalize(),
        # ),
        "champion": (
            True,
            lambda i, word, _: word.capitalize() if i == 0 else " " + word,
        ),
        # "lowcram": (
        #     True,
        #     lambda i, word, _: "@" + word if i == 0 else word.capitalize(),
        # ),
        "(criff | criffed)": (True, lambda i, word, _: word.capitalize()),
        # "tridal": (False, lambda i, word, _: word.capitalize()),
        # "title": (False, lambda i, word, _: word.capitalize()),
        "snake": (True, lambda i, word, _: word if i == 0 else "_" + word),
        # "dotsnik": (True, lambda i, word, _: "." + word if i == 0 else "_" + word),
        "smash": (True, lambda i, word, _: word),
        "squash": (False, lambda i, word, _: word),
        # "(spine | kebab)": (True, lambda i, word, _: word if i == 0 else "-" + word),
        "spine": (True, lambda i, word, _: word if i == 0 else "-" + word),
        "title": (False, title_case_capitalize_word),
    }
)

surrounders = normalise_keys(
    {
        "dubstring": (False, surround('"')),
        "quoted": (False, surround("'")),
        "glitch": (False, surround("`")),
        "padded": (False, surround(" ")),
        # "dunder": (False, surround("__")),
        "downdoor": (False, surround("__")),
        "angler": (False, surround("<", ">")),
        # "(index | brax)": (False, surround("[", "]")),
        # "kirk": (False, surround("{", "}")),
        # "precoif": (False, surround('("', '")')),
        # "(prex | args)": (False, surround("(", ")")),
    }
)

formatters.update(surrounders)


# def FormatText(m):
#     fmt = []

#     for w in m._words:
#         if isinstance(w, Word) and w != "over":
#             fmt.append(w.word)
#     words = parse_words(m)
#     if not words:
#         try:
#             with clip.capture() as s:
#                 press("cmd-c")
#             words = s.get().split(" ")
#         except clip.NoChange:
#             words = [""]

#     tmp = []

#     smash = False
#     for i, w in enumerate(words):
#         word = parse_word(w, True)
#         for name in reversed(fmt):
#             smash, func = formatters[name]
#             word = func(i, word, i == len(words) - 1)
#         tmp.append(word)

#     sep = "" if smash else " "
#     insert(sep.join(tmp))
#     # if no words, move cursor inside surrounders
#     if not words[0]:
#         for i in range(len(tmp[0]) // 2):
#             press("left")

# reverting to an old version for better nesting
def FormatText(m):
    fmt = []

    for w in m._words:
        if isinstance(w, Word) and w != "over":
            fmt.append(w.word)
    words = parse_words(m)
    if not words:
        try:
            with clip.capture() as s:
                press("cmd-c")
            words = s.get().split(" ")
        except clip.NoChange:
            words = [""]

    # Ensure multi-word phrases are single words
    tmp = []
    for word in words:
        tmp.extend(word.split())
    words = tmp

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    Str(sep.join(words))(None)


ctx = Context("formatters")

ctx.keymap(
    {
        "oh <dgndictation> [over]": text,
        "phrase <dgndictation>++ [over]": text,
        "sentence <dgndictation> [over]": [" ", sentence_text],
        "dot <dgndictation> [over]": [".", text],
        "teapot <dgndictation> [over]": ["this.", text],
        "champ <dgndictation> [over]": sentence_text,
        "marco <dgndictation> [over]": [Key("cmd-f"), text, Key("enter")],
        "assign <dgndictation> [over]": [" = ", text],
        "coal gap <dgndictation> [over]": [": ", text],
        "state import <dgndictation> [over]": ["import ", text],
        "state class <dgndictation> [over]": ["class ", text],
        "state const <dgndictation> [over]": ["const ", text],
        "state let <dgndictation> [over]": ["let ", text],
        "state function <dgndictation> [over]": ["function ", text],
        "state return": "return ",
        "state return <dgndictation> [over]": ["return ", text],
        "state while <dgndictation> [over]": ["while ()", Key("left"), text],
        "tools tag": ["<>", Key("left")],
        "tools tag and": ["</>", Key("left"), Key("left")],
        "tools tag <dgndictation> [over]": ["<", text, "> ", "</", text, ">"],
        "tools tag solo <dgndictation> [over]": [
            "<",
            text,
            "/>",
            Key("left"),
            Key("left"),
        ],
        "state (var|variable) <dgndictation> [over]": ["var ", text],
        "state (def|define) <dgndictation> [over]": ["def ", text],
        "args <dgndictation>": ["()", Key("left"), text],
        # "(comma | ,) <dgndictation> [over]": [", ", spoken_text],
        "padright <dgndictation> [over]": [spoken_text, " "],
        "swipe <dgndictation> [over]": [", ", spoken_text],
        "period <dgndictation> [over]": [". ", sentence_text],
        "word <dgnwords>": word,
        "more <dgndictation> [over]": [" ", text],
        "(%s)+ [<dgndictation>] [over]" % (" | ".join(formatters)): FormatText,
        # to match surrounder command + another command (i.e. not dgndictation)
        "(%s)+" % (" | ".join(surrounders)): FormatText,
    }
)
