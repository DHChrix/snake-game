from turtle import Turtle
ALIGN = "Center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=270)
        self.color("white")
        self.score = 0
        with open("data.text") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}  High Score = {self.high_score}",align=ALIGN, font= FONT)

    def scoring(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score = {self.high_score}",align=ALIGN, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.text", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score = {self.high_score}", align=ALIGN, font=FONT)
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGN, font= FONT)

