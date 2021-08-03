class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):
    def speak(self):
        print("Bark")


cat = Cat("Kity", 12, "brown")
cat.show()
cat.speak()

dog = Dog("Tom", 15)
dog.show()
dog.speak()