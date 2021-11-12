from turtle import Screen, Turtle, heading, position
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")

colors = ["red", "green", "blue", "purple", "pink", "DarkViolet", "aquamarine"]


# Lesson solution
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for sides in range(3, 15):
#     timmy.color(random.choice(colors))
#     draw_shape(sides)


# My solution - color picker doesn't work

# def color_value():
#     return random.randrange(0, 255)

# shape_sides = [3, 4, 5, 6, 7, 8, 9, 10]

# for shape in shape_sides:
#     r = color_value()
#     g = color_value()
#     b = color_value()
#     timmy.pencolor(r, g, b)
#     for _ in range(shape):
#         angle = 360 / shape
#         timmy.forward(100)
#         timmy.right(angle)


# Random Walk
# PROGRAM

# 1)While keep walking is True: (DONE)
# 2)Change color (DONE)
# 3)Turn to a random heading - (0,1,2,3) = ('east','north','west','south') (DONE?)
#     alt way:
#     heading = rand_dir()
#     timmy.left(heading)
# 4)Move forward 10 paces (DONE)
# 5)Check position (DONE)
#     current_position = timmy.position()
# 6)If position at y is less than 535 and greater than -535
#     And position at x is less than 639 and greater than -639
# 7)REPEAT
#     Else -keep_ walking = False

# Tangent:
#   Maybe this is right - attempt to set the number of 'degrees' in a circle
#   timmy.degrees(4)


def rand_dir():
    facings = range(0, 4)
    direction = random.choice(facings)
    return direction


timmy.position()

headings = [0, 90, 180, 270]

keep_walking = True

while keep_walking:
    timmy.color(random.choice(colors))
    timmy.left(headings[rand_dir()])
    timmy.forward(10)
    if timmy.ycor() <= 535 and timmy.ycor() >= -535 and timmy.xcor() <= 639 and timmy.xcor() >= -639:
        keep_walking = True
    else:
        keep_walking = False

screen = Screen()
screen.exitonclick()
