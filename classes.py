<<<<<<< HEAD
class Player:
    def __init__(self, persuasion, spirit, maturity, pride, love, choice):
        self.persuasion = persuasion
        self.spirit = spirit
        self.maturity = maturity
        self.pride = pride
        self.love = love
        self.choices = choice
=======
class Decision:
    def __init__(self, prompt, choices):
        self.prompt = prompt
        self.choices = choices

    def choice_amount(self):
        amnt = 0
        for x in self.choices:
            amnt += 1
>>>>>>> 39e369d3d28d3ee4f93d69ebd101fd4fcbc0b1ce

