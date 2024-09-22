from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")


#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window,
          #  image=bg
            ).place(x=0,y=0)
f=('bahnschrift',10)
ff=('Felix Titling',15)
fo=('bahnschrift',18)

#Label(window,text='',bg='grey',height=100,width=100).place(x=0,y=0)

Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)
#Label(window,text='Borrowed book details',bg='light blue',fg='blue',
     # font=ff).place(x=152,y=135)

def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import borrowedbk
    
def tomain():
    window.destroy()
    import projectmain

def bkb():
    Label(window,text='',bg='light blue',height=1000,width=1000).place(x=0,y=0)
    import mysql.connector as ani
    cntr=ani.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("SELECT * FROM borrow where status='borrowed'")
    
    Label(window,text='id',font=f,width=9,bg='green',
          fg='white').grid(row=0,column=0)
    Label(window,text='name',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=1)
    Label(window,text='book id',font=f,width=9,bg='green',
          fg='white').grid(row=0,column=2)
    Label(window,text='book name',font=f,width=22,bg='green',
          fg='white').grid(row=0,column=3)
    Label(window,text='borrowed',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=4)
    Label(window,text='returned',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=5)
    Label(window,text='status',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=6)
    i=1
    for stu in c:
        ii=0
        for j in stu:
            if stu[3]==j:
                Label(window,text=j,
                  width=9,bg='light blue',fg='blue').grid(row=i,column=ii)
            if stu[0]==j or stu[2]==j:
                Label(window,text=j,
                  width=9,bg='light blue',fg='blue').grid(row=i,column=ii)
                
            else:
                Label(window,text=j,
                  width=10,bg='light blue',fg='blue').grid(row=i,column=ii)
            ii+=1
        
        i=i+1
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

def bkr():
    Label(window,text='',bg='light blue',height=1000,width=1000).place(x=0,y=0)
    import mysql.connector as ani
    cntr=ani.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("SELECT * FROM borrow where status='returned'")
    
    Label(window,text='id',font=f,width=9,bg='green',
          fg='white').grid(row=0,column=0)
    Label(window,text='name',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=1)
    Label(window,text='book id',font=f,width=9,bg='green',
          fg='white').grid(row=0,column=2)
    Label(window,text='book name',font=f,width=22,bg='green',
          fg='white').grid(row=0,column=3)
    Label(window,text='borrowed',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=4)
    Label(window,text='returned',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=5)
    Label(window,text='status',font=f,width=10,bg='green',
          fg='white').grid(row=0,column=6)
    i=1
    for stu in c:
        ii=0
        for j in stu:
            if stu[3]==j:
                Label(window,text=j,
                  width=9,bg='light blue',fg='blue').grid(row=i,column=ii)
            if stu[0]==j or stu[2]==j:
                Label(window,text=j,
                  width=9,bg='light blue',fg='blue').grid(row=i,column=ii)
                
            else:
                Label(window,text=j,
                  width=10,bg='light blue',fg='blue').grid(row=i,column=ii)
            ii+=1
        
        i=i+1
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



    
    
def alllist():
    Label(window,text='',bg='light blue',height=1000,width=1000).place(x=0,y=0)
    import mysql.connector as ani
    cntr=ani.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("SELECT * FROM borrow")
    
    Label(window,text='USER ID',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=0)
    Label(window,text='NAME',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=1)
    Label(window,text='BOOK ID',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=2)
    Label(window,text='BOOK NAME',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=3)
    Label(window,text='BORROWED',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=4)
    Label(window,text='RETURNED',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=5)
    Label(window,text='STATUS',font=f,width=32,height=2,bg='green',
          fg='white').grid(row=0,column=6)
    i=1
    for stu in c:
        ii=0
        for j in stu:
            if stu[3]==j:
                Label(window,text=j,
                  width=32,height=2,font=f,bg='white',fg='blue').grid(row=i,column=ii)
            if stu[0]==j or stu[2]==j:
                Label(window,text=j,
                  width=32,height=2,font=f,bg='white',fg='blue').grid(row=i,column=ii)
                
            else:
                Label(window,text=j,
                  width=32,height=2,font=f,bg='white',fg='blue').grid(row=i,column=ii)
            ii+=1
        
        i=i+1
    Button(window,
       text='GO TO MAIN',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=10,y=550)

    Button(window,
       text='BACK',
       fg='yellow',
       height=2,
       command=back,
       width=20,
       bg='black').place(x=200,y=550)

def alter():
    Label(window,text='',height=500,width=500,bg='light pink').place(x=0,y=0)    
    Label(window,text='BORROING',bg='light pink',fg='black',font=ff).place(x=2,y=2)
    Label(window,text='RETURNING',bg='light pink',fg='black',font=ff).place(x=2,y=270)


    
    Label(window,text="Borrower ID",bg='light pink').place(x=10,y=40)
    Label(window,text="Borrower Name",bg='light pink').place(x=10,y=70)
    Label(window,text="Book ID",bg='light pink').place(x=10,y=100)
    Label(window,text="Book Name",bg='light pink').place(x=10,y=130)
    Label(window,text="Borrowed On",bg='light pink').place(x=10,y=160)

    Label(window,text="Borrower ID",bg='light pink').place(x=10,y=300)
    Label(window,text="Borrower Name",bg='light pink').place(x=10,y=330)
    Label(window,text="Book ID",bg='light pink').place(x=10,y=360)
    Label(window,text="Book Name",bg='light pink').place(x=10,y=390)
    Label(window,text="Returning On",bg='light pink').place(x=10,y=420)

    ai=StringVar()
    bi=StringVar()
    ci=StringVar()
    di=StringVar()
    ei=StringVar()

    ae=StringVar()
    be=StringVar()
    ce=StringVar()
    de=StringVar()
    ee=StringVar()
       
    Entry(window,width=30,textvariable=ai).place(x=110,y=40)
    Entry(window,width=30,textvariable=bi).place(x=110,y=70)
    Entry(window,width=30,textvariable=ci).place(x=110,y=100)
    Entry(window,width=30,textvariable=di).place(x=110,y=130)
    Entry(window,width=30,textvariable=ei).place(x=110,y=160)
    
    Entry(window,width=30,textvariable=ae).place(x=110,y=300)
    Entry(window,width=30,textvariable=be).place(x=110,y=330)
    Entry(window,width=30,textvariable=ce).place(x=110,y=360)
    Entry(window,width=30,textvariable=de).place(x=110,y=390)
    Entry(window,width=30,textvariable=ee).place(x=110,y=420)
    
    def borrowing():
        #global ai,bi,ci,di,ei
        aai=ai.get()
        bbi=bi.get()
        cci=ci.get()
        ddi=di.get()
        eei=ei.get()
        
        import mysql.connector as ani
        cntr=ani.connect(user='root',password='YSshalini@09',host='localhost',database='project')
        c=cntr.cursor()

        c.execute("insert into borrow values('{}','{}','{}','{}','{}',NULL,'borrowed')".format(aai,bbi,cci,ddi,eei))
        cntr.commit()
        import tkinter.messagebox
        tkinter.messagebox.showinfo("command done","one record added!")
        #Label(window,text='added!',bg='purple',fg='yellow',height=2,width=20).place(x=400,y=90)
                                                                     
 
    def returning():
        #global ae,ce
        aae=ae.get()
        cce=ce.get()
        eee=ee.get()
        import mysql.connector as ani
        cntr=ani.connect(user='root',password='YSshalini@09',host='localhost',database='project')
        c=cntr.cursor()
        c.execute("select uid,bid from borrow")
        non=0
        for i in c:
            if i[0]==aae and i[1]==cce:
                non=1
                #print("success")
                c.execute("update borrow set status='returned',dor='{}' where uid='{}' and bid='{}'".format(eee,aae,cce))
                cntr.commit()
                import tkinter.messagebox
                tkinter.messagebox.showinfo("Command Done","One Record Edited!")
        if non==0:
            import tkinter.messagebox
            tkinter.messagebox.showwarning("No Such Record Exist!","Recheck The IDs Entered")
                
    Button(window,text='borrowing',bg='BLACK',fg='YELLOW',
           command=borrowing,width=10,font=fo).place(x=50,y=185)
    Button(window,text='returning',bg='BLACK',fg='YELLOW',
           command=returning,
           width=10,font=fo).place(x=50,y=445)

        
#define stringvar and get()








    Button(window,
       text='GO TO MAIN',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=10,y=550)

    Button(window,
       text='BACK',
       fg='yellow',
       height=2,
       command=back,
       width=20,
       bg='black').place(x=200,y=550)



Button(window,
       text='VIEW ALL LIST',
       height=2,
       font=f,
       command=alllist,
       width=30).place(x=180,y=180)

Button(window,
       text='ALTER LIST',
       height=2,
       font=f,
       command=alter,
       width=30).place(x=180,y=240)

Button(window,
       text='BORROWED BOOKS',
       height=2,
       font=f,
       command=bkb,
       width=30).place(x=180,y=300)

Button(window,
       text='RETURNED BOOKS',
       height=2,
       font=f,
       width=30,
       command=bkr
       ).place(x=180,y=360)
Button(window,text='BACK',fg='yellow',height=2,command=tomain,width=20,bg='black').place(x=10,y=550)


