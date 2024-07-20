class pet(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi. I'm {self.name} \n")


pet1 = pet("Cindy")
print(pet1.name)
pet1.talk()
