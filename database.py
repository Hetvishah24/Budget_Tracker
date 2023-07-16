import sqlite3
from tkinter import *
from tkinter import messagebox as tkMessageBox

def CreateDatabase():
    global conn, c
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS 'members'(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS 'data'(name TEXT,day VARCHAR,typeex TEXT,typeda TEXT,amount TEXT)")

def insert(n):
    CreateDatabase()
    if n == "":
        tkMessageBox.showinfo("Warning", "Please enter name")
    else:
        print(n)
        c.execute("SELECT mem_id FROM members WHERE name = (?)",(n,))

        if c.fetchone() is not None:
            tkMessageBox.showinfo("Warning", "Name Already Exist")
        
        else:
            n =n.lower()
            n = n.capitalize()
            c.execute("INSERT INTO members (name) VALUES (?)",(str(n),))
            conn.commit()
            
        c.close()
        conn.close()

def database(a1, a2, a3, a4, a5):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    c.execute("INSERT INTO data (name,day,typeex,typeda,amount) VALUES (?,?,?,?,?)",
              (str(a1), str(a2), str(a3), str(a4), str(a5)))
    # c.execute('DELETE FROM bruhexpenses;',);
    print("success")
    conn.commit()
    c.close()
    conn.close()



def database_extract(m_y):
    
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    month_year = "%/%{}/{}".format(m_y[0],m_y[1])
    cursor = c.execute('SELECT name,SUM(AMOUNT) FROM data WHERE day LIKE (?) AND typeex IS NOT "HouseHold" GROUP BY name',(month_year,))
    labels=[]
    value=[]
    for row in cursor:
        labels.append(row[0])
        value.append(row[1])
    
    labels.append("Household")
    cursor = c.execute('SELECT SUM(AMOUNT) FROM data WHERE day LIKE (?) AND typeex IS "HouseHold" ',(month_year,))
    for row in cursor:
        value.append(row[0])
    return labels,value

def database_extract2(m_y,name):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    month_year = "%/%{}/{}".format(m_y[0],m_y[1])
    if name !="Household":
        
        cursor = c.execute('SELECT typeda,SUM(amount) FROM data WHERE name=? AND day LIKE (?) AND typeex IS NOT "HouseHold" GROUP BY typeda',(name,month_year,))
        labels=[]
        value=[]
        for row in cursor:
            labels.append(row[0])
            value.append(row[1])
            
        return labels,value
    
    else:
        cursor = c.execute('SELECT typeda,SUM(amount) FROM data WHERE day LIKE (?) AND typeex IS "HouseHold" GROUP BY typeda',(month_year,))
        labels=[]
        value=[]
        for row in cursor:
            labels.append(row[0])
            value.append(row[1])
            
        return labels,value


def database_extract3():
    
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    labels=[]
    value=[]
    for  i in range(9,12):
        month_year = "%/%{}/{}".format(i,2021)
        labels.append(monthDict[i])
        cursor = c.execute('SELECT SUM(amount) FROM data WHERE day LIKE (?)',(month_year,))
        for row in cursor:
            if(row[0])== None:
                value.append(0)
            else:
                value.append(row[0])
    #print(labels,value)

    return labels,value

def database_extract4(n):
    
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    labels=[]
    value=[]
    for  i in range(9,12):
        month_year = "%/%{}/{}".format(i,2021)
        labels.append(monthDict[i])
        cursor = c.execute('SELECT SUM(amount) FROM data WHERE day LIKE (?) AND name = (?)',(month_year,n,))
        for row in cursor:
            if(row[0])== None:
                value.append(0)
            else:
                value.append(row[0])
    #print(labels,value)

    return labels,value

    
def get_names(household_flag = False):
    
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    cursor = c.execute('SELECT DISTINCT(name) FROM members')
    names=[]
    for row in cursor:
        names.append(row[0])
    
    if household_flag == True:
            names.append("Household")

    return names

def delete_name(n):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    print("Delete ",n)
    cursor = c.execute('DELETE FROM members WHERE name = (?)',(n,))
    conn.commit()
    #print("success")

def renamemember(a,b):
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("UPDATE members SET name = (?) WHERE name =(?)",(b,a,))
    print("success")
    conn.commit()
    c.close()
    conn.close()


#########################Renames table: DO NOT RUN#############################
def rename():
    
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute("INSERT INTO members(name) VALUES(?)",(""))
    print("success")
    conn.commit()
    c.close()
    conn.close()

# "INSERT INTO members(name) VALUES(?)",("self",)