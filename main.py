from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

s = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.right,"Right")
screen.onkey(s.left,"Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

#     detect collision with food
    if s.head.distance(food) < 15:
        food.refresh()
        scoreboard.scoring()
        s.extend()

#       detect collision with wall
    if s.head.xcor()>280 or s.head.xcor()<-280 or s.head.ycor()>280 or s.head.ycor()<-280:
        scoreboard.reset()
        # with open("data.text", mode="w") as file:
        #     file.write(str(scoreboard.high_score))
        s.reset()
#       detect collision with tail
    for segments in s.segments[1:]:
        if s.head.distance(segments) < 10:
            scoreboard.reset()
            # with open("data.text", mode="w") as file:
            #     file.write(str(scoreboard.high_score))
            s.reset()

screen.exitonclick()