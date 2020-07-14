from typing import Tuple

import numpy as np

# tile struct compatible with Console.tiles_rgb
# ch is a unicode codepoint, this is the character for the tile
# fg is the foreground color
# bg is the background color
graphic_dt = np.dtype(
    [
        ('ch', np.int32),
        ('fg', '3B'),
        ('bg', '3B'),
    ]
)

# statically defined tile data
# walkable if you can walk over it
# transparent if it does or does not block field of view
# dark is what the tile looks like when it isnt in the field of view
tile_dt = np.dtype(
    [
        ('walkable', np.bool),
        ('transparent', np.bool),
        ('dark', graphic_dt),
        ('light', graphic_dt),
    ]
)

# creates a new tile using the structs


def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int]]
) -> np.array:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# this just draws black tile
SHROUD = np.array((ord("X"), (62, 53, 70), (46, 34, 47)), dtype=graphic_dt)


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)
