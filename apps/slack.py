import time

from talon.voice import Context, Key

from ..utils import text

ctx = Context("slack", bundle="com.tinyspeck.slackmacgap")

keymap = {
    # Channel
    "channel": Key("cmd-k"),
    "channel <dgndictation>": [Key("cmd-k"), text, Key("enter")],
    # "channel last": Key("alt-up"),
    # "([channel] unread last | gopreev)": Key("alt-shift-up"),
    # "channel last": Key("alt-shift-up"),
    # "channel next": Key("alt-down"),
    # "([channel] unread next | goneck)": Key("alt-shift-down"),
    # "channel next": Key("alt-shift-down"),
    # "[channel] info": Key("cmd-shift-i"),
    "channel info": Key("cmd-shift-i"),
    # "channel up": Key("alt-up"),
    # "channel down": Key("alt-down"),
    # Navigation
    "tools focus": Key("ctrl-`"),
    "section next": Key("f6"),
    "section previous": Key("shift-f6"),
    # "page up": Key("pageup"),
    # "page down": Key("pagedown"),
    "((open | collapse) right pane | toggle sidebar)": Key("cmd-."),
    "tools direct": Key("cmd-shift-k"),
    "tools thread": Key("cmd-shift-t"),
    "history next": Key("cmd-["),
    "history last": Key("cmd-]"),
    # "next element": Key("tab"),
    # "previous element": Key("shift-tab"),
    "tools activity": Key("cmd-shift-m"),
    "tools directory": Key("cmd-shift-e"),
    "tools stars": Key("cmd-shift-s"),
    # "unread [messages]": Key("cmd-j"),
    # "(go | undo | toggle) full": Key("ctrl-cmd-f"),
    # Messaging
    # "grab left": Key("shift-up"),
    # "grab right": Key("shift-down"),
    "new line": Key("shift-enter"),
    "slapper": [Key("cmd-right"), Key("shift-enter")],
    "tools react": Key("cmd-shift-\\"),
    # "user": Key("@"),
    # "tag channel": Key("#"),
    "tools command": Key("cmd-shift-c"),
    "tools code": [
        "``````",
        Key("left left left"),
        Key("enter"),
        Key("enter"),
        Key("up"),
    ],
    "tools bullet": Key("cmd-shift-8"),
    "tools number": Key("cmd-shift-7"),
    "tools indent": Key("cmd-shift->"),
    # "bold": Key("cmd-b"),
    # "(italic | italicize)": Key("cmd-i"),
    "(tools | tool) strike": Key("cmd-shift-x"),
    # "mark all read": Key("shift-esc"),
    # "mark channel read": Key("esc"),
    # "clear": [Key("cmd-a"), Key("backspace")],
    # Files and Snippets
    # "upload": Key("cmd-u"),
    "(tool | tools) snippet": Key("cmd-shift-enter"),
    # Calls
    # "([toggle] mute | unmute)": Key("m"),
    # "([toggle] video)": Key("v"),
    # "invite": Key("a"),
    # Miscellaneous
    "(tool | tools) status": Key("cmd-shift-y"),
    "(tool | tools) shortcut": Key("cmd-/"),
    "tools collapse": ["/collapse ", Key("enter")],
    "tools expand": ["/expand ", Key("enter")],
}

ctx.keymap(keymap)
# TODO: add git commands from original std.py
