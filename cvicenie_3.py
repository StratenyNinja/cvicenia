import tkinter
import random


# 1)
canvas = tkinter.Canvas()
canvas.pack()
x, y = 50, 50
canvas.create_rectangle(x, y, x+100, y+100, fill="red")
canvas.create_rectangle(x+110, y, x+210, y+100, fill="blue")
canvas.create_text(x+50, y+50, text="červený", font="arial 20", fill="yellow")
canvas.create_text(x+160, y+50, text="modrý", font="arial 20", fill="yellow")

# 2)
canvas = tkinter.Canvas(background="navy")
canvas.pack()
n = 200
for i in range(n):
    canvas.create_text(random.randint(0, 375), random.randint(0, 275), text="*", font=f"arial {random.randint(10, 20)}", fill="yellow")

tkinter.mainloop()