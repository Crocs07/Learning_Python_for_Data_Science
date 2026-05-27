import turtle


class MyTurtle(turtle.Turtle):
    def __init__(self, color: str = "blue", shape: str = "turtle") -> None:
        super().__init__()
        self.color(color)
        self.shape(shape)
        self._step_size = 40

    def draw_square(self, side_length: int = 100) -> None:
        for _ in range(4):
            self.forward(side_length)
            self.right(90)

    def move_step(self) -> None:
        self.forward(self._step_size)
