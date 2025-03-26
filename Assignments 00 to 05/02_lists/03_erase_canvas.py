import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<B1-Motion>", self.erase_cells)

    def create_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")
                self.cells.append(rect)

    def create_eraser(self, event):
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink")

    def erase_cells(self, event):
        if self.eraser:
            self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            overlapping = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            for obj in overlapping:
                if obj in self.cells:
                    self.canvas.itemconfig(obj, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
