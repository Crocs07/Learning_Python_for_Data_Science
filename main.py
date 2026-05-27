import turtle

from my_turtle import MyTurtle


def main() -> None:
    screen = turtle.Screen()
    screen.title("MyTurtle Demo")

    pen = MyTurtle(color="green")
    pen.speed(2)
    pen.draw_square(120)
    pen.penup()
    pen.goto(-150, 0)
    pen.pendown()
    pen.move_step()

    screen.exitonclick()


if __name__ == "__main__":
    main()
