# originally from https://github.com/JonathanNickerson/talon_voice_user_scripts
# and https://github.com/pimentel/talon_user/blob/master/repeat.py

from talon.voice import Context, Rep, RepPhrase, talon
from .. import utils

ctx = Context("repeater")


def repeat(m):
    # TODO: This could be made more intelligent:
    #         * Apply a timeout after which the command will not repeat previous actions
    #         * Prevent stacking of repetitions upon previous repetitions
    repeat_count = utils.extract_num_from_m(m)

    if repeat_count is not None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)


ctx.keymap(
    {
        # "wink": Rep(1),
        "creek": RepPhrase(1),
        "second": Rep(1),
        "third": Rep(2),
        "fourth": Rep(3),
        "fifth": Rep(4),
        # "(repeat | repple)" + utils.numerals: repeat,
        "repeat" + utils.numerals: repeat,
    }
)
