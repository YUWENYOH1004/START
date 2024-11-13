import random
class Die:
    def __init__(self, sides):
        self.sides = sides
        self.face_value = 1

    def roll(self):
        self.face_value = random.randint(1, self.sides)

    def __str__(self):
        return self.face_value

    def __add__(self, other):
        return self.face_value + other.face_value


    def get_value(self):
        return self.face_value

    def __gt__(self, other):
        return self.face_value > other.face_value


class Player:
    def __init__(self, name):
        self.name = name
        self.die6 = Die(6)
        self.die10 = Die(10)

    def roll_dice(self):
        self.die6.roll()
        self.die10.roll()

    def get_dice_value(self):
        self.roll_dice()
        return self.die6 + self.die10

    def __str__(self):
        return self.name


class HighTwoGame:
    def __init__(self, player1='', player2=''):
        self.players = [Player(player1), Player(player2)]



    def playOneGame(self):
        dice_values = []
        for player in self.players:
            rolled = player.get_dice_value()
            dice_values.append(rolled)
            print(f"{player} rolled {rolled} ")

        if dice_values[0] > dice_values[1]:
            print(f"{self.players[0]} wins! ")
        elif dice_values[0] < dice_values[1]:
            print(f"{self.players[1]} wins!")
        else:
            print("Tie")

    def playManyGames(self, numGames=1):
        wins = {
            self.players[0]: 0,
            self.players[1]: 0
        }
        for i in range(numGames):
            dice_values = []
            for player in self.players:
                rolled = player.get_dice_value()
                dice_values.append(rolled)

            if dice_values[0] > dice_values[1]:
                wins[self.players[0]] += 1
            elif dice_values[0] < dice_values[1]:
                wins[self.players[1]] += 1
            else:
                pass

        print(f"The score is {wins[self.players[0]]} to {wins[self.players[1]]}")
        max_wins = max(wins.values())
        winner = [key for key, value in wins.items() if value == max_wins]
        if len(winner) == 1:
            print(f'{winner[0]} wins!')
        else:
            print('Tie')
            
    def __str__(self):
        return f"Dice game between {self.players[0]} and {self.players[1]}"
