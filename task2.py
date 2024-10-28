import turtle
import math

def draw_pythagoras_tree(branch_length, angle, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)
    
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level - 1)
    turtle.right(2 * angle)
    
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level - 1)
    turtle.left(angle)
    turtle.backward(branch_length)

def main(level):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.left(90)
    draw_pythagoras_tree(100, 45, level)
    turtle.done()

level = int(input("Введіть рівень рекурсії: "))
main(level)
