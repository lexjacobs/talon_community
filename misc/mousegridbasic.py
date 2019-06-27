import time
from talon import ctrl, ui
from talon.voice import Context

ctx = Context("mousegridbasic")


# TODO: modify for second monitor https://talonvoice.com/docs/index.html#document-modules/ctrl
# ui.screens()[1]


def mouse_grid(m):
    positions = {
        1: (0, 0),
        2: (2, 0),
        3: (4, 0),
        4: (0, 2),
        5: (2, 2),
        6: (4, 2),
        7: (0, 4),
        8: (2, 4),
        9: (4, 4),
    }
    position = int(str(m._words[2]))
    screen_size = ui.main_screen()
    width = screen_size.width
    height = screen_size.height
    segmentx = width / 6
    segmenty = height / 6
    spokenx = positions.get(position)[0]
    spokeny = positions.get(position)[1]
    ctrl.mouse((segmentx * spokenx + segmentx), (segmenty * spokeny + segmenty))


keymap = {
    "mouse grid (1|2|3|4|5|6|7|8|9)": mouse_grid,
    "mouse grid second": lambda m: ctrl.mouse(2332.0, 389.0),
}

ctx.keymap(keymap)
