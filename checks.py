class Check():
    def __init__(self, action):
        self.action = action

    def speak(self):
        print(action)

class CheckOne(Check):
    def __init__(self):
        Check.__init__(self, "Performing the first check.")

    def apply_(self):
        self.speak()
