from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.ht()

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", False, "center", ("arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, "center", ("arial", 30, "normal"))


