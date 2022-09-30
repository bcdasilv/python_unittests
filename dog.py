class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.weight = 5
        self.is_happy = False

    def eat(self):
        print("Yuum... that was delicious")
        self.weight += 5

    def play(self):
        self.is_happy = True