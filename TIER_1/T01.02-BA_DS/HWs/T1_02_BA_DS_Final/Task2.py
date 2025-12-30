import turtle

def pithagoras_tree(t, branch_length, level):
    """
    Recursive function for drawing the tree
    """
    if level == 0:             # Base case
        return

    t.forward(branch_length)   # Draw main branch
    t.right(45)                # Turn right to draw the right sub-branch

    # Recursive for the right branch / Decrease branch length
    pithagoras_tree(t, branch_length * 0.7, level - 1)

    t.left(90)                 # Then turn left

    # Recursive for the left branch / Decrease branch length
    pithagoras_tree(t, branch_length * 0.7, level - 1)

    t.right(45)                # Back to original direction

    # Go back to the branch point
    # Turtle returns to the exact position where it started
    t.backward(branch_length)


def main():                    # Screen setup
    screen = turtle.Screen()
    screen.title("Fractal 'Pythagoras Tree'")

    t = turtle.Turtle()        # Create turtle
    t.speed(0)
    t.color("brown")
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    try:
        recursion_level = int(input("Enter recursion level (recommended 5-10): "))
    except ValueError:
        recursion_level = 7    # if input is not a number

    recursion_level = max(1, min(15, recursion_level))

    pithagoras_tree(t, 100, recursion_level)
    screen.exitonclick()


if __name__ == "__main__":
    main()