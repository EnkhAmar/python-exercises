class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    # Not specific to an instance
    # It is called on class itself
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("tim")
p2 = Person("jill")

print(Person.get_number_of_people())