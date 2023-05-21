import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Hello tkinter')
    
    root.configure(background="aqua")
    root.minsize(200, 200)  # width, height
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")  # width x height + x + y
    root.mainloop()


if __name__ == '__main__':
    main()
