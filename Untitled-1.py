import turtle

## Set up a screen

window = turtle.Screen()
window.bgcolor("lightgray")


# create a player 
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
speed = 1  # player move speed


# player movement
def virar_esq():
    player.left(30)


def para_frente():
    player.forward(15)


def virar_dir():
    player.right(30)


def para_tras():
    player.backward(15)


# keybord bindings
turtle.listen()
turtle.onkeypress(virar_esq, "Left")
turtle.onkeypress(para_frente, "Up")
turtle.onkeypress(para_tras, "Down")
turtle.onkeypress(virar_dir, "Right")

while True:
    player.forward(speed)


turtle.done()