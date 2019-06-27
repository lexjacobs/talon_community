"""
Commands that write bits of code that is valid for multiple languages
"""

from talon.voice import Context, Key

ctx = Context("general_lang")

ctx.keymap(
    {
        # Operators
        "assign": " = ",
        "(op | open) minus": " - ",
        "(op | open) plus": " + ",
        "op times": " * ",
        "op divide": " / ",
        "op colon": " : ",
        "op question": " ? ",
        "op mod": " % ",
        # "((op minus | subtract) equals | minus assign)": " -= ",
        # "((op plus | add) equals | (plus | add) assign)": " += ",
        # "([op] (times | multiply) (assign | equals) | star assign)": " *= ",
        # "[op] divide (assign | equals)": " /= ",
        # "[op] mod (assign | equals)": " %= ",
        # "(op colon (equals | assign) | coleek)": " := ",
        "(op | is) greater [than]": " > ",
        "(op | is) less [than]": " < ",
        # "((op | is) equal [to] | longqual)": " == ",
        "op equal": " == ",
        # "((op | is) not equal [to] | banquall)": " != ",
        "op not equal": " != ",
        # "((op | is) greater [than] or equal [to] | grayqual)": " >= ",
        "op greater equal": " >= ",
        # "((op | is) less [than] or equal [to] | lessqual)": " <= ",
        "op less equal": " <= ",
        # "([(op | is)] exactly (equal [to] | equals) | triple equals | trickle)": " === ",
        "trickle": " === ",
        # "([(op | is)] not exactly (equal [to] | equals) | ranqual | nockle)": " !== ",
        "op not exact": " !== ",
        "op power": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (logical | bitwise) and": " & ",
        "([op] (logical | bitwise) or | (op | D) pipe)": " | ",
        "[(op | logical | bitwise)] (ex | exclusive) or": " ^ ",
        "(op | logical | bitwise) (left shift | shift left)": " << ",
        "(op | logical | bitwise) (right shift | shift right)": " >> ",
        # "(op | logical | bitwise) and equals": " &= ",
        # "(op | logical | bitwise) or equals": " |= ",
        # "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        # "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        # "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
        "op arrow": " -> ",
        "op fat": " => ",
        # Completed matchables
        "call": "()",
        "empty object": "{}",
        "empty array": "[]",
        # Blocks
        # "[brace] block": [" {}", Key("left enter enter up tab")],
        "decked in it": ["{}", Key("left")],
        "index": ["[]", Key("left")],
        "block": ["{}", Key("left enter")],
        "block super": ["{}", Key("left enter enter up space space")],
        # "(square | brax) block": ["[", Key("enter")],
        # "(paren | prex) block": ["(", Key("enter")],
        # Combos
        "coalshock": [":", Key("enter")],
        # "comshock": [",", Key("enter")],
        "sinker": [Key("cmd-right ;")],
        # "swipe": ", ",
        "pebble": ", ",
        "coalgap": ": ",
        # "[forward] slasher": "// ",
        # Statements
        "state (def | deaf | deft)": "def ",
        "state if": "if ",
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": "for ",
        "state function": "function ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        "state const ": "const ",
        "state let": "let ",
        "state var": "var ",
        # Other Keywords
        # "const": "const ",
        # "static": "static ",
        "tip pent": "int",
        "tip char": "char",
        # "tip byte": "byte ",
        # "tip float": "float ",
        # "tip double": "double ",
        # Comments
        "comment see": "// ",
        "comment py": "# ",
        "trussell": Key("cmd-/"),
        "pixel": "px",
        "ten": "10",
        "twenty": "20",
        "thirty": "30",
        "forty": "40",
        "fifty": "50",
        "sixty": "60",
        "seventy": "70",
        "eighty": "80",
        "ninety": "90",
    }
)
