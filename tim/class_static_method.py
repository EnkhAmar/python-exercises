# I do not have to create instance of Math class to use static method.
# static = not changing
# static method do not have access to change anything

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @ staticmethod
    def pr():
        print("run")


print(Math.add5(5))
Math.pr()