from tkinter import *
from PIL import Image,ImageTk
import page2
import datanalysis


green="#91c46b"
white="#f3f3f3"
lightgrey="#34383c"
darkergrey="#1e2226"
blue="#8bc8cf"
gradient="#bee3a1"
pagenumber = 1

root=Tk()

root.title("Every Rupee")

img1 = Image.open(r"assets\algorithm.png")
img1 = img1.resize((150,150))
photo1 = ImageTk.PhotoImage(img1)

img2 = Image.open(r"assets\imageonline-co-roundcorner.png")
img2 = img2.resize((400,700))
photo2 = ImageTk.PhotoImage(img2)

img3 = Image.open(r"assets\algorithm.png")
img3 = img3.resize((150,150))
photo3 = ImageTk.PhotoImage(img3)

img4 = Image.open(r"assets\programmer.png")
img4 = img4.resize((150,150))
photo4 = ImageTk.PhotoImage(img4)

img5 = Image.open(r"assets\imageonline-co-roundcorner (1).png")
img5 = img5.resize((946,524))
photo5 = ImageTk.PhotoImage(img5)

img10 = Image.open(r"assets\family.png")
img10 = img10.resize((150,150))
photo10 = ImageTk.PhotoImage(img10)

img11 = Image.open(r"assets\personal.png")
img11 = img11.resize((150,150))
photo11 = ImageTk.PhotoImage(img11)

img12 = Image.open(r"assets\family graph.png")
img12 = img12.resize((150,150))
photo12 = ImageTk.PhotoImage(img12)


img13 = Image.open(r"assets\user graph.png")
img13 = img13.resize((150,150))
photo13 = ImageTk.PhotoImage(img13)


def go2users():

    global root , canvas0 , canvas1 , canvas2 ,canvas3 , canvas4 , canvas5 ,  L1 ,L2 ,L3 ,L4 ,L5 ,L6, B0 , B1 ,B2
    L=[canvas1 , canvas3 ,canvas4,B0,B1,B2 ] 
    page2.second_page(L , root , photo5 , mainpage )
    return




def go2data():
    global root , canvas0 , canvas1 , canvas2 ,canvas3 , canvas4 , canvas5 ,  L1 ,L2 ,L3 ,L4 ,L5 ,L6, B0 , B1 ,B2
    L=[canvas1 , canvas3 ,canvas4,B0,B1,B2 ] 
    datanalysis.second_page(L , root , photo5 , photo10 , photo11,photo12,photo13 , mainpage )
    return

def mainpage():
    global root , canvas0 , canvas1 , canvas3, canvas4 , L1, L2 , B1 ,B2 ,B0 
    root.deiconify()
    root.configure(bg=green)
    w = 1150
    h = 950

    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.resizable(0,0)

    canvas0 = Canvas(root, bg=green, width=320,height=150, highlightbackground=green)
    canvas0.create_image(150,75,image=photo1)
    
    canvas0.place(x=250,y=20)


    L1=Label(root, text  = "Every" , fg="#FFFFFF" , bg = green)
    L1.config(font=("Gotham Medium",50,'bold'))

    L1.place(x=500,y=20)

    L2=Label(root, text  = "Rupee" , fg="#FFFFFF" , bg = green)
    L2.config(font=("Gotham Medium",50,'bold'))

    L2.place(x=650,y=90)

    canvas1 = Canvas(root, bg=green,width = 500,height = 700 , highlightbackground=green)
    canvas1.create_image(250,353,image=photo2)
    canvas1.place(x=340,y=200)

    canvas3 = Canvas(root, bg="#8bc8cf",width = 150,height = 150 , highlightbackground="#8bc8cf")
    canvas3.create_image(78,90,image=photo3)
    canvas3.place(x= 520 , y = 325)

    B0 = Button(root,text="Menu",bg="#8bc8cf",width=56,height=2,borderwidth=0)
    B0.place(x= 390 , y = 250)

    B1 = Button(root,text="Data Analytics",bg="#8bc8cf",command = go2data,width=56,height=2 )
    B1.place(x= 390 , y = 520)

    canvas4 = Canvas(root, bg="#8bc8cf",width = 150,height = 150 , highlightbackground="#8bc8cf")
    canvas4.create_image(78,90,image=photo4)
    canvas4.place(x= 520 , y = 615)

    B2 = Button(root,text="User ID",bg="#8bc8cf",command = go2users,width=56,height=2 )
    B2.place(x= 390 , y = 800)

mainpage()

root.mainloop()