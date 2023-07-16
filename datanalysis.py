from tkinter import *
from tkcalendar import Calendar
from database import database,database_extract,get_names,database_extract2,database_extract3,database_extract4
import matplotlib.pyplot as plt
import numpy

green="#91c46b"
white="#f3f3f3"
lightgrey="#34383c"
darkergrey="#1e2226"
blue="#8bc8cf"
gradient="#bee3a1"
pagenumber = 2

def overall_pie():
    def get_month():
        global month
        month = cal.get_displayed_month()
        popup.quit()
        popup.destroy()

    popup = Tk()
    popup.title("Select Date")
    popup.focus_force()
    caution = Label(popup, text="Select day of the month you want to view",fg="red").pack()
    cal = Calendar(popup, selectmode='day')
    cal.pack()
    submitb = Button(popup, text="Submit", command=get_month).pack()
    popup.mainloop()
    
        
    labels,values =database_extract(month)

    def absolute_value(val):
        a  = numpy.round(val/100.*(numpy.array(values)).sum(), 0)
        return a
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct=absolute_value,
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()



def individ_pie():
    def get_month():
        global month
        month = cal.get_displayed_month()
        popup.quit()
        popup.destroy()

    popup = Tk()
    popup.title("Select Date")
    popup.focus_force()
    caution = Label(popup, text="Select day of the month you want to view",fg="red").pack()
    cal = Calendar(popup, selectmode='day')
    cal.pack()
    submitb = Button(popup, text="Submit", command=get_month).pack()
    popup.mainloop()

    def get_member():
        global name
        name = variable.get()
        popup.quit()
        popup.destroy()

    
    list_options = get_names(True)
    popup = Tk()
    popup.title("Select Member")
    popup.focus_force()
    askname = Label(popup , text = "Select Member").pack()
    variable = StringVar(popup)
    variable.set(list_options[0])
    drop = OptionMenu(popup , variable , *list_options )
    drop.config(width=20, font=('Helvetica', 12)) 
    drop.pack()
    submit = Button(popup , text = "Submit" , command= get_member ).pack()
    popup.mainloop()
  
    
    labels,values =database_extract2(month,name)

    def absolute_value(val):
        a  = numpy.round(val/100.*(numpy.array(values)).sum(), 0)
        return a
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct=absolute_value,
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def overall_line():
    labels,values =database_extract3()
    #print(labels,values)
    
    plt.bar(labels,values)
    plt.show()

def individ_line():
    def get_member():
        global name
        name = variable.get()
        popup.quit()
        popup.destroy()

    
    list_options = get_names()
    popup = Tk()
    popup.title("Select Member")
    popup.focus_force()
    askname = Label(popup , text = "Select Member").pack()
    variable = StringVar(popup)
    variable.set(list_options[0])
    drop = OptionMenu(popup , variable , *list_options )
    drop.config(width=20, font=('Helvetica', 12)) 
    drop.pack()
    submit = Button(popup , text = "Submit" , command= get_member ).pack()
    popup.mainloop()

    labels,values =database_extract4(name)
    print(labels,values)
    
    plt.bar(labels,values)
    plt.show()

def second_page(L,root,photo5,photo6,photo7,photo8,photo9 ,mainpage ):
    def backb():
        def all_children (wid) :
            _list = wid.winfo_children()

            for item in _list :
                if item.winfo_children() :
                    _list.extend(item.winfo_children())
            return _list
        widget_list = all_children(root)
        
        for item in widget_list:
                item.destroy()
        root.withdraw()
        mainpage()
        
    global b3 , b4 , b5 , b6 , L3 , L4 , L5 , L6 , canvas5 

    global members 

    for i in L:
        i.place_forget()
    root.geometry("1150x850")
    root.resizable(0,0)
    
    
    
    canvas5 = Canvas(root , bg=blue , width = 1000 , height = 570 , highlightbackground=green)
    canvas5.create_image(498,290,image=photo5)
    canvas5.place(x= 80 , y = 200)
    members = ["Monthly PieChart" , "7-Day Graph" ]

    b3 = Button(root, image = photo6, bg="#afdbaf",width = 200,height = 200 , borderwidth = 0 , highlightbackground="#8bc8cf" , command = overall_pie )
    b3.place(x = 155 , y = 300)

    b4 = Button(root,image = photo7, bg="#95cdc6",width = 200,height = 200 , borderwidth = 0 , highlightbackground="#8bc8cf", command= individ_pie)
    b4.place(x = 380 , y = 300)

    b5 = Button(root,image = photo8, bg="#85c4d4",width = 200,height = 200 , borderwidth = 0 , highlightbackground="#8bc8cf", command= overall_line)
    b5.place(x = 605 , y = 300)

    b6 = Button(root,image = photo9, bg="#69b6f0",width = 200,height = 200 , borderwidth = 0 , highlightbackground="#8bc8cf" ,command= individ_line)
    b6.place(x = 830 , y = 300)


    L3=Label(root, text  = members[0] , fg="#FFFFFF" , bg = "#afdbaf", width = 17)
    L3.config(font=("Gotham Medium",18))
    L3.place(x = 113 , y = 502)

    L4=Label(root, text  = members[0] , fg="#FFFFFF" , bg = "#95cdc6", width = 15)
    L4.config(font=("Gotham Medium",18))
    L4.place(x = 380 , y = 502)

    L5=Label(root, text  = members[1] , fg="#FFFFFF" , bg = "#85c4d4", width = 14)
    L5.config(font=("Gotham Medium",18))
    L5.place(x = 606 , y = 502)

    L6=Label(root, text  = members[1] , fg="#FFFFFF" , bg = "#68b5f0", width = 14)
    L6.config(font=("Gotham Medium",18))
    L6.place(x = 830 , y = 502)
    back = Button(root , text = "Back" , bg="#91c46b",width = 10 ,height = 2 , borderwidth = 1 , highlightbackground="#bfe49f", command= backb )

   
    back.place(x = 2 , y = 203)


    return