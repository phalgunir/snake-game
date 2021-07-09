from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.setposition(0, 280)
        self.speed('fastest')

        self.score = 0
        with open('data.txt', mode='r') as high_score_file:
            self.high_score = int(high_score_file.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.print_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as high_score_file:
                high_score_file.write(f'{self.high_score}')
        self.print_score()
        self.score = 0
