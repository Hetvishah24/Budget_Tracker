from tkinter import *
from tkcalendar import Calendar
import database

green="#91c46b"
white="#f3f3f3"
lightgrey="#34383c"
darkergrey="#1e2226"
blue="#8bc8cf"
gradient="#bee3a1"
personal = ["Select Option" , "Clothing", "Eating at Restaurents", "Entertainment" , "Travel" , "Others" ]
household = ["Select Option" , "Groceries" , "Bill Payments" , "Maintanence" , "Utilities" , "Others" ]
check = 0 
a=0

def submitbutton():
    global cal , typeex , typeda , amount_text , x1 , check , a , a1
    root =  x1
    print(type(a1))
    a2 = cal.get_date()
    print(a2)
    a3 = typeex
    a4 = typeda
    a5 = amount_text.get()
    if a5 =="":
        print("failed")
        check=0

    if check == 1:

        l_0 = ["#c0e49e","#68b5f0"]
        if a == 1:
            L7=Label(root, text="Success!" , fg="#FFFFFF" , bg = l_0[0], width = 7)
            L7.config(font=("Gotham Medium",20))
            L7.place(x = 871 , y = 652)
            a=0
        else:
            L7=Label(root, text="Success!" , fg="#FFFFFF" , bg = l_0[1], width = 7)
            L7.config(font=("Gotham Medium",20))
            L7.place(x = 871 , y = 652)
            a=1

        database.database(a1,a2,a3,a4,a5)
    print(a1,a2,a3,a4,a5)


def addmember():
    global x2
    def text():
        global x2
        n = entry.get()
        database.insert(n)
        root= x1
        root.quit()
        second_page(l,root , Photo5 , x2 )
        top.quit()
        top.destroy()

    top= Tk()

    top.focus_force()
    top.geometry("200x50")
    top.title("Add Member")
    top.config(bg = green )
    entry= Entry(top, width= 50)
    entry.pack()
    b = Button(top,text= "Insert",command= text).pack(pady= 5,side=TOP)
    top.mainloop()
    
def delmember():
    global x2
    def get_member():
        global name
        name = variable.get()
        database.delete_name(name)
        root= x1
        root.quit()
        second_page(l,root , Photo5 , x2 )
        popup.quit()
        popup.destroy()

    
    list_options = database.get_names()
    popup = Tk()
    popup.title("Select Member to Delete")
    #popup.geometry("200x80")
    popup.config(bg = green)
    #askname = Label(popup , text = "Select Member").pack()
    variable = StringVar(popup)
    variable.set(list_options[0])
    drop = OptionMenu(popup , variable , *list_options )
    drop.config(width=20, font=('Helvetica', 12)) 
    drop.pack()
    submit = Button(popup , text = "Delete" , command= get_member ).pack(pady= 5,side=TOP)
    popup.mainloop()

def renamemem():
    global x2

    def get_member():
        global name
        name = variable.get()
        nn = entry.get()
        database.renamemember(name,nn)
        
        root= x1
        root.quit()
        second_page(l,root , Photo5 , x2 )
        popup.quit()
        popup.destroy()
        

    list_options = database.get_names()
    popup = Tk()
    popup.title("Select Member to Rename")
    # popup.geometry("200x80")
    popup.config(bg=green)
    # askname = Label(popup , text = "Select Member").pack()
    variable = StringVar(popup)
    variable.set(list_options[0])
    drop = OptionMenu(popup, variable, *list_options)
    drop.config(width=20, font=('Helvetica', 12))
    drop.pack()
    entry = Entry(popup, width=50)
    entry.pack()
    submit = Button(popup, text="Rename", command=get_member).pack(pady=5, side=TOP)
   

    popup.mainloop()


   
   
def second_page(L,root,photo5,mainpage):

    
    global drop , clicked , x1 ,l , Photo5 ,x2 ,a1
    global cal , naam , typeex , typeda , amount_text , x1 , check 
    for i in L:
        i.place_forget()
    root.geometry("1150x850")
    root.resizable(0,0)
    x2 = mainpage
    def backb():
        def all_children (root) :
            global _list
            _list = root.winfo_children()

            for item in _list :
                if item.winfo_children() :
                    _list.extend(item.winfo_children())
                    return _list
        widget_list = all_children(root)
        for item in widget_list:
                item.place_forget()
        root.withdraw()
        mainpage()

    def get_a1(drop):
        global a1
        drop = clicked.get()
        a1 = drop
    l = L





    Photo5 = photo5
    canvas5 = Canvas(root , bg=blue , width = 1000 , height = 570 , highlightbackground=green)
    canvas5.create_image(498,290,image=photo5)
    canvas5.place(x= 80 , y = 200)

    x1 = root

    Title=Label(root, text  = "Data Entry  " , fg="#FFFFFF" , bg = "#afdbae")
    Title.config(font=("Gotham Medium",30))
    Title.place(x = 111 , y = 252)

    name=Label(root, text  = "Member", fg="#FFFFFF" , bg = "#afdbae")
    name.config(font=("Gotham Medium",20))
    name.place(x = 110 , y = 352)
    
    options = database.get_names()
    clicked = StringVar()

    drop = OptionMenu( root , clicked , *options , command = get_a1)
    drop.config(bg = green , highlightbackground=blue , width = 19 )
    drop.place(x= 250 , y =352)

    date=Label(root, text  = " Date :" , fg="#FFFFFF" , bg = "#bae1a4")
    date.config(font=("Gotham Medium",20))
    date.place(x = 110 , y = 452)
    
    cal = Calendar(root, selectmode = 'day',date_pattern='dd/mm/y')
    cal.place(x = 200 , y = 452)

    add = Button(root , text = "Add Member" , bg="#91c46b",width = 10 ,height = 2 , borderwidth = 1 , highlightbackground="#bfe49f", command= addmember )
    add.place(x = 900 , y = 800)

    dele = Button(root , text = "Delete Member" , bg="#91c46b",width = 15 ,height = 2 , borderwidth = 1 , highlightbackground="#bfe49f", command= delmember )
    dele.place(x = 768 , y = 800)
    
    


    rename = Button(root , text = "Rename", bg="#91c46b",width = 10 ,height = 2 , borderwidth = 1 , highlightbackground="#bfe49f" ,command=renamemem)
    rename.place(x = 1000 , y = 800)
    
    canvas = Canvas (root , width = 6 , height = 300 )
    canvas.create_line(1, 3, 3, 400 , width = 5 , fill = "#bce2a3")
    canvas.config(bg = "#8cc8ce", highlightbackground= "#8cc8ce" )
    canvas.place(x=600 , y = 300)


    desc = Label (root , text = "Type : ", fg="#FFFFFF" , bg = "#79bee1")
    desc.config(font=("Gotham Medium",20))
    desc.place(x = 680 , y = 352)




    def selection():
        global personal , household ,menu , optionmenu , check , typeex , typeda , amount_text , expenses , amount
        a , b = var1.get() , var2.get()
        variable = StringVar(root)
        expenses = Label(root , text = "Expenses : " , fg = "white" , bg = "#79bee1" )
        expenses.config(font=("Gotham Medium",20))
        expenses.place(x=680 , y = 475)
        def optdata(data):
            global typeda ,check , amount_text
            data = variable.get()
            typeda = data
            amount = Label(root , text = "Amount in Rs. : ", fg="#FFFFFF" , bg = "#79bee1")
            amount.config(font=("Gotham Medium",20))
            amount_text = Entry ( root , width = 20 )
            amount.place (x= 680 , y = 600)
            amount_text.place(x = 900 , y = 610)
            check = 1
            return

        if ( a == 1 and b == 0  ):
            menu = OptionMenu( root , variable  , *personal , command = optdata )
            menu.config(bg = blue , highlightbackground=blue , width = 19 )
            menu["menu"].config(bg = "#bce2a3" )
            variable.set(personal[0])
            typeex = "Personal"
            menu.place(x=840 , y = 480)          
            householdB.config(state = DISABLED )
        elif (a == 0 and b == 1 ):
            menu = OptionMenu( root , variable  , *household , command = optdata )
            menu.config(bg = blue , highlightbackground=blue , width = 19 )
            menu["menu"].config(bg = "#bce2a3" )
            variable.set(household[0])
            menu.place(x=840 , y = 480)
            typeex = "HouseHold"
            personalB.config( state = DISABLED )
        else:
            menu.destroy()
            personalB.config(state = "normal" )
            householdB.config(state = "normal" )
            typeex = ""



       

        return
    var1=IntVar()
    var2=IntVar()
    personalB = Checkbutton(root, bg= blue , text = "Personal" , variable = var1 , onvalue=1 , offvalue= 0  , command = selection )
    householdB = Checkbutton(root , bg= blue , text = "HouseHold" , variable = var2 , onvalue=1 , offvalue= 0 , command = selection )
    personalB.place( x = 780 , y = 362)
    householdB.place( x = 900 , y = 362)
    submit = Button(root , text = "Submit" ,  bg="#85c5d5",width = 20,height = 5 , borderwidth = 1 , highlightbackground="#bfe49f" , command = submitbutton )
    submit.place(x = 535 , y = 650)

    back = Button(root , text = "Back" , bg="#91c46b",width = 10 ,height = 2 , borderwidth = 1 , highlightbackground="#bfe49f", command= backb )

   
    back.place(x = 2 , y = 203)
    




    return