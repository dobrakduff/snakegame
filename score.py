from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.count}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.count += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))