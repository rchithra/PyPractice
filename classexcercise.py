class Fruit(object):

    def __init__(self):
        print("I am a fruit")

    def nutrition(self):
        print("I am full of nutrition. ")

    def fruit_shape(self):
        print("I am available in various shapes")


class Mango(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("I am Mango")

    def nutrition(self):
        print("I am full of vitamin C")

    def color(self):
        print("I come in various shades of yellow")


f = Fruit()
f.nutrition()
f.fruit_shape()

m = Mango()
m.nutrition()
m.fruit_shape()
m.color()

