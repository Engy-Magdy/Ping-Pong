from turtle import Turtle,Screen
class Score(Turtle):
   def __init__(self,goto):
      super().__init__()
      self.score=0
      self.color("white")
      self.penup()
      self.goto(goto)
      self.write(f"{self.score}",font=("arial",50,"normal"))
      self.hideturtle()
   def point(self):
      self.score+=1
      self.clear()
      self.write(f"{self.score}",font=("arial",50,"normal"))
