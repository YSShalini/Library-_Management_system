from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")
f=('bahnschrift',10)
#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window,
          #  image=bg
            ).place(x=0,y=0)
Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)


def tomain():
    window.destroy()
    import projectmain

def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import carddetail
    
def backk():
    window.destroy()
    import userdetail

def username():
    window.destroy()
    import searchusername

def userid():
    window.destroy()
    import searchuserid




    
def userlist():
    Label(window,
      text='',
      bg='light blue',
      height=100,
      width=100).place(x=0,y=0)
    import mysql.connector as a
    cntr=a.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("select * from user")

    Label(window, text='user list',
                  bg='purple',fg='white',width=15).grid(row=0,column=0)
    Label(window, text='ID',
                      bg='green',fg='white',width=15).grid(row=1,column=0)
    Label(window, text='user name',
                      bg='green',fg='white',width=18).grid(row=1,column=1)
    Label(window, text='age',
                      bg='green',fg='white',width=15).grid(row=1,column=2)
    Label(window, text='joined on',
                      bg='green',fg='white',width=15).grid(row=1,column=3)
    Label(window, text='phone',
                      bg='green',fg='white',width=20).grid(row=1,column=4)
    cc=2
    for i in c:
        ccc=0
        for j in i:
            
                #print("works")
            Label(window,text=j,
                      bg='light blue',
                      width=15).grid(row=cc,column=ccc)
            ccc+=1
                #Label(window,text=j).grid(row=ccc,column=1)
        cc+=1
    Button(window,
       text='Go to main',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=10,y=550)
    Button(window,
       text='Back',
       fg='yellow',
       height=2,
       command=backk,
       width=20,
       bg='black').place(x=200,y=550)




Button(window,
       text='view all users',
       height=2,
       font=f,
       command=userlist,
       width=30).place(x=180,y=180)

Button(window,
       text='Find using user name',
       height=2,
       font=f,
       command=username,
       width=30).place(x=180,y=240)

Button(window,
       text='Find using user ID',
       height=2,
       font=f,
       command=userid,
       width=30).place(x=180,y=300)

Button(window,
       text='Back',
       height=2,
       font=f,
       width=30,
       command=back
       ).place(x=180,y=360)

