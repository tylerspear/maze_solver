from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__running = False