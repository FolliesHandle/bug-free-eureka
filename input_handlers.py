# pythons type hinting system
from typing import Optional

# importing tcod's event system and the action subclasses
import tcod.event
from actions import Action, EscapeAction, MovementAction

# this is a subclass of EventDispatch, which allows us to send an event to its proper method


class EventHandler(tcod.event.EventDispatch[Action]):
    # recieves a quit event, and exits the system
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # recieves keypress events,

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        # holds the subclass of action that we assign it to, if none is assigned it will remain set to none
        action: Optional[Action] = None
        # holds the key press
        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action
