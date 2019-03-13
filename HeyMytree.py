#Is there a surprise
#It's a gift for you ~

import turtle

def draw_branch(branch_length):
    if branch_length > 22:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 7)

        turtle.left(40)
        draw_branch(branch_length - 7)

        turtle.right(20)
        turtle.backward(branch_length)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(120)
    turtle.pendown()
    turtle.pensize(7)
    turtle.pencolor('darkgreen')
    draw_branch(77)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
