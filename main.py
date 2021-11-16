import random
import threading
import time
from tkinter import *
from random import *

X, Y = 700, 300
SIZE = 100
COLORS = ["#fc0345", "#fc0335", "#fc032c", "#fc031c", "#e80046"]
COLORS_RIGHT = ["#4bf720", "#20f724", "#20f724", "#20f72f", "#20f739"]

pos = []

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{X}x{Y}")
        self.root.resizable(True, False)
        self.root.title("Visualizing Sorting Algorithm")
        self.mainFrame = self.createMainFrame()
        self.c = self.createCanvas()
        self.rects = self.createRects()
        threading.Thread(target=self.sort).start()

    def sort(self):
        time.sleep(0.8)
        sizes = {}
        for l in self.rects:
            i, size, color = l[2], l[1], l[3]
            sizes[i] = size
            self.c.itemconfig(i, fill="#00ff00")
            time.sleep(0.02)
            self.c.itemconfig(i, fill=color)

        x11, x22 = 0, X/SIZE
        for j in range(SIZE-3):
            _min = min(sizes, key=sizes.get)
            x1, y1, x2, y2 = self.c.coords(_min)

            for k,v in sizes.items():
                if k < int(_min):
                    x1, y1, x2, y2 = self.c.coords(k)
                    self.c.coords(k, x1+X/SIZE, y1, x2+X/SIZE, y2)
            x1, y1, x2, y2 = self.c.coords(_min)

            self.c.coords(_min, x11, y1, x22, y2)
            x11 += X/SIZE; x22 += X/SIZE
            self.c.itemconfig(_min, fill=choice(COLORS_RIGHT))
            del sizes[_min]
            time.sleep(0.02)

    def createRects(self):
        rects = []
        x1 = 0
        x2 = x1+X/SIZE
        y2 = 300
        used = []
        for i in range(SIZE):
            _color = choice(COLORS)
            y1 = randint(90, 270)
            while y1 in used:
                y1 = randint(90, 270)
            used.append(y1)
            _rect = self.c.create_rectangle(x1, y1, x2, 300, fill=_color)
            pos.append([x1, y1, x2, 300])
            x1 += X/SIZE
            x2 = x1+X/SIZE
            rect_size = Y-y1
            rects.append([len(rects)+1, rect_size, _rect, _color])
        for i in [0, -1, -2]:
            self.c.delete(rects[i][2])

        del rects[0]
        del rects[-1]
        del rects[-1]

        return rects

    def createCanvas(self):
        c = Canvas(self.mainFrame, width=680, height=290, bg="#ffffff")
        c.place(x=10, y=10)
        return c

    def createMainFrame(self):
        frame = Frame(self.root, bg="#ffffff")
        frame.pack(fill="both", expand="True")
        return frame

    def loop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.loop()