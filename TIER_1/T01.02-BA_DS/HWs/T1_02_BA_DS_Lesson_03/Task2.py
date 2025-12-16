import turtle 

def koch_curve(t, level, size):
    if level == 0:            # base case
        t.forward(size)       # draw a line
    else:                     # snowflake
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, size / 3) 
            t.left(angle)


def draw_koch_snowflake(level, size=300):
    screen = turtle.Screen()  # create window
    screen.bgcolor("black")   # background color

    t = turtle.Turtle()       # create turtle
    t.speed(0)                # max speed
    t.color("white")          # line's color

    t.penup()                 # do not draw
    t.goto(-size / 2, 0)      # move turtle in position
    t.pendown()               # start drawing

    for _ in range(3):        # triangle with 3 sides
        koch_curve(t, level, size)
        t.right(120)

    screen.mainloop()         # keep window open


def main():
    level = int(input("Enter recursion level (0-7): "))  # user input level
    draw_koch_snowflake(level)  


if __name__ == "__main__":
    main()
