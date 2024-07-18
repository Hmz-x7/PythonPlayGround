#some examples on inheritance 


class Wolf: 
    def __init__(self, name , color): 
        self.name = name 
        self.color = color  

    def bark(self): 
        print("Grrr....")

class Dog(Wolf):
    def bark (self):
        print("Woof woof !!")

class Coyote(Wolf):
    def __init__(self, name, color,sound):
        super().__init__(name, color)
        self.sound = sound 

    def bark(self):
        print(self.sound + " tuee tuee hehe!!")

class Boerboel(Dog):
    def description(self):
        print("Hell big crazy MF\nthese powerful farm dogs can weigh up to 130 pounds and are known for their strength and dominance.")

class GreatDane (Dog):
    def description(self):
        print("Despite their gentle giant reputation,\nGreat Danes can weigh up to 200 pounds and are alert guards, but not overly aggressive.")


co = Coyote("tork" , "brown" , "kee ke ekek")

co.bark()

dog = Dog("marloat", "yellow")
dog.bark()

wol = Wolf("nxi" , "gray")

wol.bark()
print(wol.name)





bor = Boerboel("CJ","black")
bor.bark()
bor.description()

Pell = GreatDane("Pell", "brown&white")

Pell.bark()
Pell.description()