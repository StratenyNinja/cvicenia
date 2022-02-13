import tkinter


canvas = tkinter.Canvas()
canvas.pack()

# 1)
x, y = 50, 50
canvas.create_rectangle(x, y, x+100, y+100, fill="red")
canvas.create_rectangle(x+110, y, x+210, y+100, fill="blue")
canvas.create_text(x+50, y+50, text="červený", font="arial 20", fill="yellow")
canvas.create_text(x+160, y+50, text="modrý", font="arial 20", fill="yellow")


tkinter.mainloop()