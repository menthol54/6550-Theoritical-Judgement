class Decision:
    def __init__(self, prompt, choices):
        self.prompt = prompt
        self.choices = choices

    def choice_amount(self):
        k = 0
        for x in self.choices:
            k += 1
