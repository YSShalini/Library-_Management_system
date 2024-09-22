from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")
f=('bahnschrift',16)
#bg=PhotoImage(file='C:/comp project-library/BGs/blurr(gif).gif')
label=Label(window,
          #  image=bg
            ).place(x=0,y=0)

def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import books
def addagain():
    window.destroy()
    import adding


             
def success():
    Label(window,text='',bg='light blue',height=20,width=70).place(x=50,y=145)
    Label(window, text='added succesfully!',height=3,bg='green',fg='white',
          width=40).place(x=150,y=265)
    Button(window,
       text='Go to main',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=30,y=550)
    Button(window,
       text='View books',
       fg='yellow',
       height=2,
       command=back,
       width=20,
       bg='black').place(x=220,y=550)
    Button(window,
       text='add books',
       fg='yellow',
       height=2,
       command=addagain,
       width=20,
       bg='black').place(x=410,y=550)


    
Label(window,text='',bg='light blue',height=20,width=70).place(x=50,y=145)

Label(window,text='*must fill',bg='light blue',fg='red').place(x=350,y=165)
Label(window,text='book id',bg='light blue',font=f).place(x=140,y=160)
Label(window,text='book name',bg='light blue',font=f).place(x=106,y=190)
Label(window,text='author name',bg='light blue',font=f).place(x=89,y=220)
Label(window,text='publications',bg='light blue',font=f).place(x=95,y=250)
Label(window,text='dop',bg='light blue',font=f).place(x=173,y=280)
Label(window,text='cost',bg='light blue',font=f).place(x=166,y=310)
Label(window,text='pages',bg='light blue',font=f).place(x=150,y=340)
Label(window,text='copies',bg='light blue',font=f).place(x=148,y=370)

o=StringVar()
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()

name=Entry(window,textvariable=o).place(x=220,y=168)
name=Entry(window,textvariable=a).place(x=220,y=198)
name=Entry(window,textvariable=b).place(x=220,y=228)
name=Entry(window,textvariable=c).place(x=220,y=258)
name=Entry(window,textvariable=d).place(x=220,y=288)
name=Entry(window,textvariable=e).place(x=220,y=318)
name=Entry(window,textvariable=f).place(x=220,y=348)
name=Entry(window,textvariable=g).place(x=220,y=378)

def addbk():
    global a,b,c,d,e,f,g,o
    
    oo=o.get()
    aa=a.get()
    bb=b.get()
    cc=c.get()
    dd=d.get()
    ee=e.get()
    ff=f.get()
    gg=g.get()
    
    import mysql.connector as A
    cntr=A.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    cu=cntr.cursor()
    if aa.lower()=='null':
        cu.execute("insert into books values(null,'{}','{}','{}',{},{},{}.'{}')".format(bb,cc,dd,ee,ff,gg,oo))
    if bb.lower()=='null':
        cu.execute("insert into books values('{}',null,'{}','{}',{},{},{},'{}')".format(aa,cc,dd,ee,ff,gg,oo))
    if cc.lower()=='null':
        cu.execute("insert into books values('{}','{}',null,'{}',{},{},{},'{}')".format(aa,bb,dd,ee,ff,gg,oo))
    if dd.lower()=='null':
        cu.execute("insert into books values('{}','{}','{}',null,{},{},{},'{}')".format(aa,bb,cc,ee,ff,gg,oo))
    if aa.lower()!='null' and bb.lower()!='null' and cc.lower()!='null' and dd.lower()!='null':
        cu.execute("insert into books values('{}','{}','{}','{}',{},{},{},'{}')".format(aa,bb,cc,dd,ee,ff,gg,oo))
    cntr.commit()
    cu.execute('select * from books where name="{}"'.format(aa))
    for i in cu:
              if i[1]==bb:
                  success()

Button(window,text='add',bg='green',fg='white',height=5,width=15,
       command=addbk).place(x=380,y=250)
Button(window,
       text='Go to main',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=30,y=550)
Label(window,text='mention "null" for the missing datas',
      bg='blue',fg='white').place(x=200,y=420)
