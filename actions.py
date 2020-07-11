# class definitions for actions


class Action:
    pass


class EscapeAction(Action):
    pass


# movement action as an object with dx and dy
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
