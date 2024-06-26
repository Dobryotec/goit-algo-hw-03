import turtle

def draw_colored_line(length, color, width, level):
    turtle.pencolor(color)
    turtle.pensize(width)
    if level == 0:
        turtle.forward(length)
    else:
        new_length = length / 3.0
        draw_colored_line(new_length, color, width, level - 1)
        turtle.left(60)
        draw_colored_line(new_length, color, width, level - 1)
        turtle.right(120)
        draw_colored_line(new_length, color, width, level - 1)
        turtle.left(60)
        draw_colored_line(new_length, color, width, level - 1)

def koch_snowflake(level, length, color, width):
    for _ in range(3):
        draw_colored_line(length, color, width, level)
        turtle.right(120)

try:
    level = int(input("Enter the recursion level (positive integer): "))
    if level < 0:
        raise ValueError()
except ValueError:
    print("Please enter a positive integer.")
    exit()

turtle.bgcolor("#FFFFFF") 
turtle.speed(0)
turtle.penup()
turtle.goto(-150, 90)
turtle.pendown()

koch_snowflake(level, 300, "blue", 2)

turtle.hideturtle() 
turtle.done()