import tkinter
import random


## 1)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 50, 50 # alebo 120, 10
#canvas.create_rectangle(x, y, x+100, y+100, fill="red")
#canvas.create_rectangle(x+110, y, x+210, y+100, fill="blue")
#canvas.create_text(x+50, y+50, text="červený", font="arial 20", fill="yellow")
#canvas.create_text(x+160, y+50, text="modrý", font="arial 20", fill="yellow")
#
## 2)
#canvas = tkinter.Canvas(background="navy")
#canvas.pack()
#n = 200
#for i in range(n):
#    canvas.create_text(random.randint(0, 375), random.randint(0, 275), text="*", font=f"arial {random.randint(10, 20)}", fill="yellow")
#
## 3)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 50, 50     # alebo 140, 20
#a1, a2 = 180, 100 # alebo 200, 190
#canvas.create_rectangle(x, y, x+a1, y+a1, fill="indian red")
#canvas.create_rectangle(x+(a1-a2)/2, y+(a1-a2)/2, x+(a1-a2)/2+a2, y+(a1-a2)/2+a2, fill="light blue")
#canvas.create_text(x-10, y-10, text="A", font="arial 10")
#canvas.create_text(x+a1+10, y-10, text="B", font="arial 10")
#canvas.create_text(x-10, y+a1+10, text="C", font="arial 10")
#canvas.create_text(x+a1+10, y+a1+10, text="D", font="arial 10")
#canvas.create_text(x+a1+10, y+a1/2, text=a1, font="arial 10")
#canvas.create_text(x+a1/2, y+a1/2+a2/2-10, text=a2, font="arial 10")
#
## 4)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 150, 150
#n = 20
#f1, f2, f3 = "red", "blue", "yellow"
#for i in range(n*5, 0, -5):
#    canvas.create_rectangle(x-i, y-i, x+i, y+i, fill=f1)
#    f1, f2, f3 = f2, f3, f1
#
## 5)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 10, 10
#sirka, vyska = 135, 90
#canvas.create_rectangle(x, y, x+sirka, y+vyska, fill="yellow")
#canvas.create_rectangle(x, y, x+sirka, y+vyska*2/3, fill="red")
#canvas.create_rectangle(x, y, x+sirka, y+vyska/3, fill="black")
#canvas.create_rectangle(x+sirka+25, y, x+2*sirka+25, y+vyska, fill="red")
#canvas.create_rectangle(x+sirka+25, y, x+sirka+25+sirka*2/3, y+vyska, fill="white")
#canvas.create_rectangle(x+sirka+25, y, x+sirka+25+sirka/3, y+vyska, fill="green")
#canvas.create_rectangle(x, y+vyska+25, x+sirka, y+2*vyska+25, fill="red")
#canvas.create_rectangle(x, y+vyska+25, x+sirka*2/3, y+2*vyska+25, fill="white")
#canvas.create_rectangle(x, y+vyska+25, x+sirka/3, y+2*vyska+25, fill="blue")
#canvas.create_rectangle(x+sirka+25, y+vyska+25, x+2*sirka+25, y+2*vyska+25, fill="red")
#canvas.create_rectangle(x+sirka+25, y+vyska+25, x+2*sirka+25, y+vyska+25+vyska*2/3, fill="blue")
#canvas.create_rectangle(x+sirka+25, y+vyska+25, x+2*sirka+25, y+vyska+25+vyska/3, fill="white")
#
## 6)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 180, 250
#sirka, vyska = 200, 50
#for farba in "darkgreen", "green", "yellowgreen", "limegreen":
#    canvas.create_rectangle(x-sirka/2, y, x+sirka/2, y-vyska, fill=farba)
#    sirka -= 50
#    y -= 50
#
## 7)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 10, 100
#n, d = 16, 20
#for i in range(n):
#    canvas.create_line(x, y, x+abs(d), y+d, width="5", fill="blue")
#    x += abs(d)
#    y += d
#    d = -d
#
## 8)
#canvas = tkinter.Canvas()
#canvas.pack()
#x, y = 70, 100 # stred prveho kruhu
#r, w = 50, 15
#dx, dy = 120, 60
#for farba in "blue", "yellow", "black", "limegreen", "red":
#    canvas.create_oval(x-r, y-r, x+r, y+r, width=w, outline=farba)
#    x += dx/2
#    y += dy
#    dy = -dy

tkinter.mainloop()