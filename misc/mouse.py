# from https://github.com/talonvoice/examples
# jsc added shift-click, command-click, and voice code compatibility

# import eye
import time
from talon import ctrl, tap, ui
from talon.voice import Context, Key

ctx = Context("mouse")

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)


def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def delayed_click(m, button=0, times=1):
    # old = eye.config.control_mouse
    # eye.config.control_mouse = False
    # x, y = click_pos(m)
    # ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    # time.sleep(0.032)
    # eye.config.control_mouse = old


# jsc added
def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)


# jsc added
def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)


def option_click(m, button=0, times=1):
    press_key_and_click(m, "alt", button, times)


def delayed_right_click(m):
    delayed_click(m, button=1)


def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)


def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)


def mouse_scroll(amount):
    def scroll(m):
        ctrl.mouse_scroll(y=amount)

    return scroll


def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)


def mouse_center(m):
    win = ui.active_window()
    rect = win.rect
    center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
    print(rect, center)
    ctrl.mouse_move(*center)


keymap = {
    # jsc modified with some voice-code compatibility
    # "righty": delayed_right_click,
    "click right": delayed_right_click,
    # "(click | chiff)": delayed_click,
    "click left": delayed_click,
    # "(dubclick | duke)": delayed_dubclick,
    "click double": delayed_dubclick,
    # "(tripclick | triplick)": delayed_tripclick,
    "click triple": delayed_tripclick,
    "mouse (hold | press)": mouse_drag,
    "click hold": mouse_drag,
    "(mouse | click) release": mouse_release,
    # jsc added
    # "(shift click | shicks)": shift_click,
    "click shift": shift_click,
    # "(command click | chom lick)": command_click,
    "click command": command_click,
    "click option": option_click,
    # "wheel down": mouse_scroll(200),
    # "wheel up": mouse_scroll(-200),
    "click double cut": [lambda m: ctrl.mouse_click(button=0, times=2), Key("cmd-x")],
    "click double copy": [lambda m: ctrl.mouse_click(button=0, times=2), Key("cmd-c")],
    "click double paste": [lambda m: ctrl.mouse_click(button=0, times=2), Key("cmd-v")],
    "mouse corner": lambda m: ctrl.mouse(0, 0),
    "(mouse | move) up": lambda m: ctrl.mouse(0, 0, dx=0, dy=-10),
    "(mouse | move) right": lambda m: ctrl.mouse(0, 0, dx=10, dy=0),
    "(mouse | move) left": lambda m: ctrl.mouse(0, 0, dx=-10, dy=0),
    "(mouse | move) down": lambda m: ctrl.mouse(0, 0, dx=0, dy=10),
    "scroll down": lambda m: ctrl.mouse_scroll(y=ui.active_window().frame.height / 2),
    "scroll up": lambda m: ctrl.mouse_scroll(y=-ui.active_window().frame.height / 2),
    "scroll left": lambda m: ctrl.mouse_scroll(x=-ui.active_window().frame.width / 2),
    "scroll right": lambda m: ctrl.mouse_scroll(x=ui.active_window().frame.width / 2),
    "mouse (center | middle)": mouse_center,
}

ctx.keymap(keymap)
