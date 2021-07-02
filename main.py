import turtle
import time
import random

wn = turtle.Screen() # Se crea la pantalla
wn.title("SNAKE")
wn.bgcolor("black") # Background color
wn.setup(width=600,height=600)
wn.tracer(0)

#Score
score_user=0

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,0)

#Snake
snake = turtle.Turtle()
snake.speed(0) # Speed of animation it is the maximum
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(100,0)
snake.direction = "stop"

#Score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-280,250)
score.write("Score: "+ str(score_user), font=("Courier",25,"normal"))

segments = []

#Functions
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_down():
    if snake.direction != "up":
        snake.direction="down"

def snake_right():
    if snake.direction != "left":
        snake.direction="right"

def snake_left():
    if snake.direction != "right":
        snake.direction="left"

#Keyboard binding
wn.listen()
wn.onkeypress(snake_up,"Up")
wn.onkeypress(snake_down,"Down")
wn.onkeypress(snake_right,"Right")
wn.onkeypress(snake_left,"Left")

delay = 0.1

# Main Game loop
while True:
    wn.update()

    time.sleep(delay)

    if (snake.direction == "up"):
        y = snake.ycor()
        y = y + 20
        snake.sety(y)

    if (snake.direction == "down"):
        y = snake.ycor()
        y = y - 20
        snake.sety(y)

    if (snake.direction == "right"):
        x = snake.xcor()
        x = x + 20
        snake.setx(x)

    if (snake.direction == "left"):
        x = snake.xcor()
        x = x - 20
        snake.setx(x)

    # Checar si la serpiente golpea las paredes
    if (snake.xcor() > 290) or (snake.xcor() < -290) or (snake.ycor() > 290) or (snake.ycor() < -290):
        score.clear()
        score.write("Perdiste", font=("Courier", 25, "normal"))
        snake.direction = "stop"
        time.sleep(5)
        for segment in segments:
            segment.goto(1000, 1000)  # out of range
            # clear the segments
        segments.clear()
        snake.goto(0,0)
        score_user=0
        score.clear()
        score.write("Score:" + str(score_user), font=("Courier", 25, "normal"))


    # Snake in the same position as the food
    if (snake.ycor() == food.ycor()) and (snake.xcor() == food.xcor()):
        # Cambiar el marcador
        score_user = score_user + 10
        score.clear()
        score.write("Score:" + str(score_user), font=("Courier", 25, "normal"))

        # Cambiar de lugar la comida
        value_x = random.randrange(-280, 300, 20)
        value_y = random.randrange(-280, 300, 20)
        food.setx(value_x)
        food.sety(value_y)

        # add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to head
    if len(segments)>0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)
