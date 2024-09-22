from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1916x1080")
f=('bahnschrift',15)
#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window).place(x=0,y=0)


def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import carddetail
def backk():
    window.destroy()
    import searchuserid


Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)

Label(window,
      text='enter user id',font=f).place(x=230,y=200)
Label(window,
      text=':',font=f,bg='light blue').place(x=215,y=242)


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
       command=back,
       width=20,
       bg='black').place(x=200,y=550)
def find():
    global booknm
    gbknm=booknm.get()
    Label(window,
      text='',
      bg='light blue',
      height=40,
      width=100).place(x=0,y=0)

    Button(window,
       text='Go to main',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=10,y=550)
    Button(window,
       text='Back',fg='yellow',bg='black',
       height=2,
       width=20,
       command=backk
       ).place(x=180,y=550)

    #Button(window,text='Back',fg='yellow',height=2,command=back,width=20,bg='black').place(x=200,y=550)


    import mysql.connector as a
    cntr=a.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    cc=2


    c.execute("select * from user where id='{}'".format(gbknm))
    lv=0
    for i in c:
        lv+=1
    lvv=str(lv)
    Label(window, text=lvv+' record found',
                  bg='purple',fg='white',width=16).grid(row=0,column=0)


    c.execute("select * from user where id='{}'".format(gbknm))
    Label(window, text='no record found',
                      bg='red',fg='yellow',width=60,height=1).place(x=0,y=22)
    #print(i,i[0])
    for i in c:

        if gbknm==i[0]:
            ccc=0
            Label(window, text='user ID',
                      bg='green',fg='white',width=16).grid(row=1,column=0)
            Label(window, text='user name',
                      bg='green',fg='white',width=16).grid(row=1,column=1)
            Label(window, text='age',
                      bg='green',fg='white',width=16).grid(row=1,column=2)
            Label(window, text='joined on',
                      bg='green',fg='white',width=16).grid(row=1,column=3)
            Label(window, text='phone',
                      bg='green',fg='white',width=16).grid(row=1,column=4)
            for j in i:
                
        
            
                #print("works")
                Label(window,text=j,
                      bg='pink',
                      width=16).grid(row=cc,column=ccc)
                ccc+=1
                #Label(window,text=j).grid(row=ccc,column=1)
        cc+=1
        
            
                
    #if gbknm=="good":
        #Label(window,text='it worked!!!!').place(x=10,y=10)
    #else:
        #Label(window,text='get lost').place(x=10,y=10)
    
booknm=StringVar()    
bknm=Entry(window,width=20,textvariable=booknm).place(x=230,y=250)


btn=Button(window,text='get',
           command=find,
           height=2,
           bg='green',
           fg='white',
           width=25).place(x=200,y=320)



