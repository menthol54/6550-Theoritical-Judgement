class Decision:
    def __init__(self, prompt, choices):
        self.prompt = prompt
        self.choices = choices

    def choice_amount(self):
        amnt = 0
        for x in self.choices:
            amnt += 1

