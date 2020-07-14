#!/usr/bin/env python3

import tcod

from entity import Entity
from engine import Engine
from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon

# screen width and height, will be a json loading style later
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# map width and height
MAP_WIDTH = 80
MAP_HEIGHT = 45

# room width, height, and amount
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30


def main() -> None:
    # this tells tcod what font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    # event handler initialization
    event_handler = EventHandler()

    # initializing player as an entity
    player = Entity(int(SCREEN_WIDTH / 2),
                    int(SCREEN_HEIGHT / 2), "A", (255, 255, 255))
    npc = Entity(int(SCREEN_WIDTH / 2 - 5),
                 int(SCREEN_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms = MAX_ROOMS,
        room_min_size = ROOM_MIN_SIZE,
        room_max_size = ROOM_MAX_SIZE,
        map_width = MAP_WIDTH,
        map_height = MAP_HEIGHT,
        player = player,
    )

    engine = Engine(entities=entities,
                    event_handler=event_handler, game_map=game_map, player=player)
    # this creates the screen, its title, the tileset
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title="bug-free-eureka",
        vsync=True
    ) as context:
        # this creates the "console" (what we will be drawing to)
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")

        # game loop
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == '__main__':
    main()
