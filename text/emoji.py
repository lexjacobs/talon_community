import time

from talon.voice import Context, press
from talon import clip
from .. import utils
from ..utils import is_in_bundles, normalise_keys, paste_text
from ..bundle_groups import BROWSER_BUNDLES

EMOJI_BUNDLES = ("com.tinyspeck.slackmacgap", *BROWSER_BUNDLES)

# ctx = Context("emoji", func=is_in_bundles(EMOJI_BUNDLES))
ctx = Context("emoji")

emoji_pictures = {
    "check": lambda x: paste_text("✔️"),
    "clap": lambda x: paste_text("👏"),
    "cool": lambda x: paste_text("😎"),
    "fingers": lambda x: paste_text("🤞"),
    "fire": lambda x: paste_text("🔥"),
    "heart": lambda x: paste_text("❤️"),
    "hi five": lambda x: paste_text("🙌"),
    "magic": lambda x: paste_text("✨"),
    "okay": lambda x: paste_text("👌"),
    "party": lambda x: paste_text("🎉"),
    "peace": lambda x: paste_text("☮️"),
    "pray": lambda x: paste_text("🙏"),
    "sleep": lambda x: paste_text("😴"),
    "smile": lambda x: paste_text("🙂"),
    "teeth": lambda x: paste_text("😬"),
    "thumbs down": lambda x: paste_text("👎"),
    "thumbs up": lambda x: paste_text("👍"),
    "tongue": lambda x: paste_text("😛"),
    "wave": lambda x: paste_text("👋"),
}


emojis = normalise_keys(
    {
        "check": ":heavy_check_mark:",
        "clap": ":clap:",
        "cool": ":sunglasses:",
        "fingers": ":crossed_fingers:",
        "fire": ":fire:",
        "heart": ":heart:",
        "magic": ":sparkles:",
        "(okay hand | okay)": ":ok_hand:",
        "party": ":tada:",
        "plus": ":heavy_plus_sign:",
        "pray": ":pray:",
        "shrug": lambda x: paste_text(r"¯\_(ツ)_/¯"),
        "smile": ":slightly_smiling_face:",
        "thumbs up": ":+1:",
        "tongue": ":stuck_out_tongue:",
        "wave": ":wave:",
    }
)


def react(m):
    key = utils.join_words(m._words[1:])
    emojis[key]

    old_clipboard = clip.get()

    try:
        press("cmd-a", wait=2000)
        time.sleep(0.25)
        press("cmd-c", wait=2000)
        time.sleep(0.25)
        old_text = clip.get()

        utils.insert("+" + emojis[key])
        press("enter", wait=2000)

        if old_clipboard != old_text:
            press("cmd-a", wait=2000)
            time.sleep(0.25)
            utils.insert(old_text)
    finally:
        clip.set(old_clipboard)


keymap = {
    "emo {}".format(name): representation for name, representation in emojis.items()
}
keymap.update(
    {
        "emo print {}".format(name): representation
        for name, representation in emoji_pictures.items()
    }
)
keymap.update(
    {
        "react {}".format(utils.select_single(emojis.keys())): react,
        # 'react {}'.format(name): ['+'+representation]
        # for name, representation in emojis.items()
    }
)


ctx.keymap(keymap)
