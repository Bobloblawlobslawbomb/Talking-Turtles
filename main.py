from turtle import Screen, Turtle, colormode, heading, position
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")

timmy.pensize(15)
timmy.speed("fastest")

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Lesson solution

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for sides in range(3, 20):
#     timmy.color(random_color())
#     draw_shape(sides)


# My solution

# shape_sides = [3, 4, 5, 6, 7, 8, 9, 10]

# for shape in shape_sides:
#     timmy.color(random_color())
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


# My Solution
# headings = [0, 90, 180, 270]

# timmy.pensize(15)
# timmy.speed("fastest")

# keep_walking = True

# while keep_walking:
#     timmy.color(random_color())
#     timmy.setheading(random.choice(headings))
#     timmy.forward(50)
#     if timmy.ycor() <= 535 and timmy.ycor() >= -535 and timmy.xcor() <= 639 and timmy.xcor() >= -639:
#         keep_walking = True
#     else:
#         keep_walking = False

# The lessons:
# timmy.pensize(15)
# timmy.speed("fastest")

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(40)
#     timmy.setheading(random.choice(headings))


# Getting that random color to work

# headings = [0, 90, 180, 270]

# keep_walking = True

# while keep_walking:
#     timmy.color(random_color())
#     timmy.setheading(random.choice(headings))
#     timmy.forward(50)
#     if timmy.ycor() <= 535 and timmy.ycor() >= -535 and timmy.xcor() <= 639 and timmy.xcor() >= -639:
#         keep_walking = True
#     else:
#         keep_walking = False


# Spirograph Lesson

for degree in range(0, 18):
    for n in range(50, 201, 50):
        timmy.color(random_color())
        timmy.circle(n)
        timmy.left(5)


screen = Screen()
screen.exitonclick()
