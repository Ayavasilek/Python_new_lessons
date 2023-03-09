import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

for r in range(5, 96, 5):
    if r % 2 == 0:
        color = 'red'
    else:
        color = 'grey'
    canvas.create_oval(150-r, 100-r, 150+r, 100+r,outline=color)

window.mainloop()