import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview()
        self.tree.pack(side="top", fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        for i in range(10):
            self.tree.insert("", "end", text="Item %s" % i)

        self.root.mainloop()

    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree.selection():
            item_text = self.tree.item(item,"text")
            print(item_text)

if __name__ == "__main__":
    app = App()
