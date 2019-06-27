from talon.voice import Context, Key
from talon import macos
import os

ctx = Context("system")

ctx.keymap(
    {
        "(prefies | preferences)": Key("cmd-,"),
        "put computer to sleep": lambda m: os.system("pmset sleepnow"),
        # Requires activation of System Preferences -> Shortcuts -> Input Sources
        # -> "Select the previous input source"
        "change language": Key("ctrl-space"),
        "tools screen capture": Key("cmd-shift-4"),
        "tools screen copy": Key("cmd-ctrl-shift-4"),
        "(mission control | switch all)": lambda m: macos.dock_notify(
            "com.apple.expose.awake"
        ),
        "expose": lambda m: macos.dock_notify("com.apple.expose.front.awake"),
        "space last": Key("ctrl-alt-cmd-left"),
        "space next": Key("ctrl-alt-cmd-right"),
        "launchpad": lambda m: macos.dock_notify("com.apple.launchpad.toggle"),
        "desktop show": lambda m: macos.dock_notify("com.apple.showdesktop.awake"),
    }
)
