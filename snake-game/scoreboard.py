from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        with open("C:\\Users\\admin\\Desktop\\Python Projects\\snake-game\\data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            # self.high_score = self.score
            with open("C:\\Users\\admin\\Desktop\\Python Projects\\snake-game\\data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.goto(0, -10)
            self.write(arg=f"New High Score: {self.score}", align=ALIGNMENT, font=FONT)    
        self.game_over()
        

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)