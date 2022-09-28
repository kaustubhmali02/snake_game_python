from turtle import Turtle

SCORE_INCREMENT = 2
SCORE_BOARD_X_POSITION = 0
SCORE_BOARD_Y_POSITION = 270
SCORE_BOARD_TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(SCORE_BOARD_X_POSITION, SCORE_BOARD_Y_POSITION)
        self.penup()
        self.color(SCORE_BOARD_TEXT_COLOR)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += SCORE_INCREMENT
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)
