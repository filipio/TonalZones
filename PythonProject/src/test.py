import numpy as np

class Warrior:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def __str__(self):
        return f"warrior {self.name} with {self.attack} attack"


class Memento:
    def __init__(self, warrior):
        self.warrior = warrior

    def __str__(self):
        return self.warrior.__str__()

img = np.array([[2,3,4], [4,5,2], [3,3,3]])

elements = []
warrior = Warrior("Ben", 40)
elements.append(warrior)
elements.append(img)
memento_w = Memento(warrior)
memento_img = Memento(img)

print(warrior)
print(img)

warrior.name = "Fred" # we are modifying the same object that is on the list
img[0,:] = 0

print("first element of elements list : ", elements[0])
print("memento w : ", memento_w)
print("second element of elements list : \n", elements[1])
print("memento img : \n", memento_img)


