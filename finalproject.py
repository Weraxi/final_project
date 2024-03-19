import random
from tkinter import *
window = Tk()
window.title("Палитра")
window.geometry("1080x920")
class Red:
    image = PhotoImage(file="img/red.png").subsample(9, 9)
    def __add__(self, other):
        if isinstance(other, Yellow):
            return Orange
        elif isinstance(other, Green):
            return Yellow
        elif isinstance(other, Blue):
            return Pink
        elif isinstance(other, Violet):
            return Redviol
class Yellow:
    image = PhotoImage(file="img/yellow.png").subsample(6, 6)
    def __add__(self, other):
        if isinstance(other, Red):
            return Orange
        elif isinstance(other, Green):
            return Lightgreen
        elif isinstance(other, Blue):
            return Green
        elif isinstance(other, Violet):
            return Grey
class Green:
    image = PhotoImage(file="img/green.png").subsample(3, 3)
    def __add__(self, other):
        if isinstance(other, Red):
            return Yellow
        elif isinstance(other, Yellow):
            return Lightgreen
        elif isinstance(other, Blue):
            return Turquoise
        elif isinstance(other, Violet):
            return Darkgreen
class Blue:
    image = PhotoImage(file="img/blue.png").subsample(8, 8)
    def __add__(self, other):
        if isinstance(other, Red):
            return Pink
        elif isinstance(other, Yellow):
            return Green
        elif isinstance(other, Blue):
            return Turquoise
        elif isinstance(other, Violet):
            return Indigo
class Violet:
    image = PhotoImage(file="img/violet.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Red):
            return Redviol
        elif isinstance(other, Yellow):
            return Grey
        elif isinstance(other, Blue):
            return Indigo
        elif isinstance(other, Green):
            return Darkgreen
class Orange:
    image = PhotoImage(file="img/orange.png").subsample(4, 4)
    def __add__(self, other):
        pass
class Pink:
    image = PhotoImage(file="img/pink.png").subsample(2, 2)
    def __add__(self, other):
        pass
class Redviol:
    image = PhotoImage(file="img/redviol.png").subsample(2, 2)
    def __add__(self, other):
        pass
class Lightgreen:
    image = PhotoImage(file="img/lightgreen.png").subsample(5, 5)
    def __add__(self, other):
        pass
class Grey:
    image = PhotoImage(file="img/grey.png").subsample(6, 6)
    def __add__(self, other):
        pass
class Turquoise:
    image = PhotoImage(file="img/turquoise.png").subsample(6, 6)
    def __add__(self, other):
        pass
class Darkgreen:
    image = PhotoImage(file="img/darkgreen.png").subsample(5, 5)
    def __add__(self, other):
        pass
class Indigo:
    image = PhotoImage(file="img/indigo.png").subsample(2, 2)
    def __add__(self, other):
        pass
canvas = Canvas(window, width=1080, height=920)
canvas.pack()
elements = [Red(), Yellow(), Green(), Blue(), Violet()]
for element in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=element.image)
def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_id) == 2:
        element_id_1, element_id_2 = images_id[0], images_id[1]
        element_1 = elements[element_id_1 - 1]
        element_2 = elements[element_id_2 - 1]
        new_element = element_1 + element_2
        if new_element not in elements:
            canvas.create_image(event.x, event.y, image=new_element.image)
            elements.append(new_element)
    canvas.coords(images_id, event.x, event.y)
window.bind("<B1-Motion>", move)
window.mainloop()