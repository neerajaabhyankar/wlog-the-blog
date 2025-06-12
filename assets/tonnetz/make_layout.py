import json
import numpy as np
from libmogra import tonnetz
from typing import Tuple

Sa = 207.652349

gs = tonnetz.EFGenus.from_list(tonnetz.GT_GENUS)
tn = tonnetz.Tonnetz(gs)


def coord_to_keyboard(tonnetz_x, tonnetz_y) -> str:
    """
    tonnetz tiled left (i.e. Y-axis is t-g-b and not y-g-v on the keyboard)
    rooted at Sa = g
    """
    keyboard_arr = [
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"],
        ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]
    ]
    if tonnetz_x < -4 or tonnetz_x > 5 or tonnetz_y < -1 or tonnetz_y > 1:
        return ""
    try:
        keymap = keyboard_arr[1 - tonnetz_y][tonnetz_x + 4]
    except IndexError:
        return ""
    return keymap

def coord_to_ui(tonnetz_x: int, tonnetz_y: int) -> Tuple[int, int]:
    return (
        500 + 50*tonnetz_x - 8*tonnetz_y,
        300 - 50*tonnetz_y
    )

key_data = []
for node_ratio, node_name, node_coord in zip(tn.node_ratios, tn.node_names, tn.node_coordinates):
    keymap = coord_to_keyboard(*node_coord)
    if len(keymap) == 0:
        # we won't make this key available
        continue
    
    pos_x, pos_y = coord_to_ui(*node_coord)
    key_data.append({
        "id": str(node_ratio),
        "display_name": node_name,
        "display_color": tn.get_node_color(node_coord),
        "x": pos_x,
        "y": pos_y,
        "freq": Sa * float(node_ratio),
        "keymap": keymap
    })

with open("keyboard/key_layout.json", "w") as f:
    json.dump(key_data, f, indent=4)
