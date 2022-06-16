import os
import random
from tkinter import *
import tkinter.messagebox as mb

imgExtension = ["png", "jpeg", "jpg", "gif"] #расширение файлов
allImages = list()
rolled = list()
Brolled = list()
f = "img" #папочка с пикчами
def chooseRandomImage(directory): 
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice]
    return chosenImage

def obnul():
    ans = mb.askyesno(title='АнтиМискилк v2.0', message='Уверен, что хочешь сбросить?')
    if ans:
        rolled.clear()
def click():
    index = open(f"index.html", "w")
    index.write("<meta http-equiv='Refresh' content='1' />\n") #автообновление
    index.write("<style>\n")
    if(isOn.get() == 0):
        index.write("body{\ndisplay:none;\n}\n")
        return
    index.write(
    """
    img{
        width: 340px;
        margin: 8px;
    }
    .s{
        position: relative;
        text-align: center;
        width: 1280px;
        margin: 0 auto;
        top: 20%;
    }
    """
    )
    index.write("\n</style>\n")
    index.write("\n<div class='s'>\n")
    ini = int(count.get())
    Brolled.clear()
    while ini > 0:
        z = chooseRandomImage(f)
        ini=ini-1
        if z not in rolled:
            a = f"{f}/{z}"
            rolled.append(z)
            Brolled.append(z)
            index.write(f"<img src='{a}'>\n")
            # print(z)
        else:
            ini=ini+1
            # print("повтор ",ini)
    # print("ПЕРЕД: ",rolled)
    if len(rolled) > 5:
        rolled.clear()
        rolled.extend(Brolled)
    # print("ПОСЛЕ: ",rolled)
    index.write("\n</div>\n")
    index.close()

root = Tk()
root.title("Overlay_HDC")
root.geometry("140x80")
root.resizable(width=0, height=0)
root.attributes('-toolwindow', True)
root.bind("<F11>", lambda event: root.attributes("-topmost", not root.attributes("-topmost")))
root.bind("<F12>", lambda event: root.attributes("-topmost", False))
count = StringVar()
isOn =IntVar()

on = Checkbutton(text="Вкл/Выкл", variable=isOn)
on.place(relx=.3, rely=.2, anchor="c")

c = Entry(textvariable=count, width="5", justify="center")
c.insert(0, "5")
c.place(relx=.8, rely=.2, anchor="c")


btn = Button(text="РАНДОМ!!", background="#555", foreground="#ccc", font="16", command=click)
btn.place(relx=.5, rely=.6, anchor="c")

root.mainloop()
