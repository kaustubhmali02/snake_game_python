from turtle import Turtle

SCORE_INCREMENT = 2
SCORE_BOARD_X_POSITION = 0
SCORE_BOARD_Y_POSITION = 270
SCORE_BOARD_TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


def read_high_score():
    with open("data.txt", mode="r") as file:
        high_score = file.read()
    return high_score


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(SCORE_BOARD_X_POSITION, SCORE_BOARD_Y_POSITION)
        self.penup()
        self.color(SCORE_BOARD_TEXT_COLOR)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        high_score = read_high_score()
        self.write(f"Score = {self.score} |  High score = {high_score}", False, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += SCORE_INCREMENT
        high_score = int(read_high_score())
        if self.score > high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)
