import turtle

# Set up screen
win = turtle.Screen()
win.title("Pong by You")
win.bgcolor("green")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "k")
win.onkeypress(paddle_b_down, "l")
# Game loop
try:
    while True:
        win.update()

        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            score_a += 1
            pen.clear()
            pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        if ball.xcor() < -390:
            score_b += 1
            pen.clear()
            pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle collision
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1

except turtle.Terminator:
    print("Game closed. Thanks for playing!")