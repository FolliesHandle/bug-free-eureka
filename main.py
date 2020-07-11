import tcod


from actions import Action, EscapeAction, MovementAction

from input_handlers import EventHandler

# screen width and height, will be a json loading style later
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# entrypoint


def main() -> None:
    # player position
    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)

    # this tells tcod what font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    # event handler initialization
    event_handler = EventHandler()

    # this creates the screen, its title, the tileset
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title="Roguelike with out DeprecationWarning",
        vsync=True
    ) as context:
        # this creates the "console" (what we will be drawing to)
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")

        # game loop
        while True:
            # puts the @ symbol in its proper place
            root_console.print(x=player_x, y=player_y, string='@')

            # this updates the screen
            context.present(root_console)

            # clears console
            root_console.clear()

            # allows quitting without crashing
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == '__main__':
    main()
