"""
YUWENYOH ANKINIMBOM NFI
3/22/22

This program imports my module and logic for the game.
"""

from DiceGameClasses import *


print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
game1.playOneGame()

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.playOneGame()
