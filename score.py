from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.count} Highscore : {self.high_score}" , align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.count += 1
        self.display_score()

    def reset(self):
        if self.high_score < self.count:
            self.high_score = self.count
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.display_score()