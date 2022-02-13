import tkinter
import random


# 1)
canvas = tkinter.Canvas()
canvas.pack(side="left")
x, y = 50, 50 # alebo 120, 10
canvas.create_rectangle(x, y, x+100, y+100, fill="red")
canvas.create_rectangle(x+110, y, x+210, y+100, fill="blue")
canvas.create_text(x+50, y+50, text="červený", font="arial 20", fill="yellow")
canvas.create_text(x+160, y+50, text="modrý", font="arial 20", fill="yellow")

# 2)
canvas = tkinter.Canvas(background="navy")
canvas.pack(side="left")
n = 200
for i in range(n):
    canvas.create_text(random.randint(0, 375), random.randint(0, 275), text="*", font=f"arial {random.randint(10, 20)}", fill="yellow")

# 3)
canvas = tkinter.Canvas()
canvas.pack(side="left")
x, y = 50, 50     # alebo 140, 20
a1, a2 = 180, 100 # alebo 200, 190
canvas.create_rectangle(x, y, x+a1, y+a1, fill="indian red")
canvas.create_rectangle(x+(a1-a2)/2, y+(a1-a2)/2, x+(a1-a2)/2+a2, y+(a1-a2)/2+a2, fill="light blue")
canvas.create_text(x-10, y-10, text="A", font="arial 10")
canvas.create_text(x+a1+10, y-10, text="B", font="arial 10")
canvas.create_text(x-10, y+a1+10, text="C", font="arial 10")
canvas.create_text(x+a1+10, y+a1+10, text="D", font="arial 10")
canvas.create_text(x+a1+10, y+a1/2, text=a1, font="arial 10")
canvas.create_text(x+a1/2, y+a1/2+a2/2-10, text=a2, font="arial 10")

# 4)
canvas = tkinter.Canvas()
canvas.pack()
x, y = 150, 150
n = 20
f1, f2, f3 = "red", "blue", "yellow"
for i in range(n*5, 0, -5):
    canvas.create_rectangle(x-i, y-i, x+i, y+i, fill=f1)
    f1, f2, f3 = f2, f3, f1

tkinter.mainloop()