class person:
    def __init__(self, name, age, gender) -> None: # class constructor
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
            print("This is ",self.name,", a ",self.gender," aged ",self.age,".", sep="")

intro = person("Denise", 23, "female")
intro.introduction()
