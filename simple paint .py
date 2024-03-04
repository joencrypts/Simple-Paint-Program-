import tkinter as tk
from tkinter.colorchooser import askcolor

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Program")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.color = "black"
        self.line_width = 2
        self.old_x = None
        self.old_y = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_canvas)
        self.file_menu.add_command(label="Save", command=self.save_canvas)

        self.color_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Color", menu=self.color_menu)
        self.color_menu.add_command(label="Choose Color", command=self.choose_color)

        self.size_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Size", menu=self.size_menu)
        self.size_menu.add_command(label="Increase Size", command=self.increase_size)
        self.size_menu.add_command(label="Decrease Size", command=self.decrease_size)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line((self.old_x, self.old_y, x, y), width=self.line_width, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        color = askcolor(color=self.color)[1]
        if color:
            self.color = color

    def increase_size(self):
        self.line_width += 1

    def decrease_size(self):
        if self.line_width > 1:
            self.line_width -= 1

    def new_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode="color")

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = SimplePaint(root)
    root.mainloop()
