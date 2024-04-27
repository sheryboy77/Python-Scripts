import pickle
class Shape:
    def __init__(self, name):
        self.__name = name
    def __del__(self):
        print("Shape deleted")
    def out(self):
        print(self.__name)
    def set(self, newname):
        self.__name = newname


shape1 = Shape("square")
shape1.out()
shape1.set("circle")
shape1.out()
del shape1

time = datetime.now()

print(time)
