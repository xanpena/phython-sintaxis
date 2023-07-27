import turtle

#print help(turtle)

def main(turtle):
    turtle.begin_fill()
    make_rectangle(turtle)
    turtle.end_fill()
    turtle.mainloop()


def make_rectangle(turtle):
    length = int(input('Lado del cuadrado?: '))

    for i in range(4):
        make_line_and_turn(turtle, length)

def make_line_and_turn(turtle, length):
    turtle.speed(1)
    turtle.forward(length)
    turtle.left(90)


if __name__ == '__main__':
   print main(turtle)
