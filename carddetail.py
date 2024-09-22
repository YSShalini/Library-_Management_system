from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")
f=('bahnschrift',15)
#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window,
            #image=bg
            ).place(x=0,y=0)
Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)


def main():
    window.destroy()
    import projectmain
    
def userdetails():
    window.destroy()
    import userdetail


    
def passwordentry(ps):
    Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)
    paswrd=StringVar()
    adnm=Label(window,text='enter password',
           bg='light blue',
           fg='black',font=f).place(x=210,y=200)
    code=Entry(window,width=20,textvariable=paswrd,
               show='*').place(x=220,y=250)
    def compa():
        passw=paswrd.get()
        x=passw
        #print('passw=',passw,'ps=',ps)
        if x==ps:
            userdetails()
        
    Button(window,text='enter',width=20,height=2,command=compa,
       bg='green',fg='white'
           ).place(x=207,y=370)
    




        
def checking():#a=id   b=name
    n=0

    import mysql.connector as a
    cntr=a.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("select * from admin")
    nam=naame.get()
    nm=nam.lower()
    aid=admid.get()
    for i in c:
        #print(i,aid,nm)
        if i[0]==aid:
            #print(i[0],'i[o]')
            if i[1]==nm:
                n+=1
                ps=i[2]
                passwordentry(ps)
    if n==0:
        Label(window,text="admin id and name doesnt match",
                  bg='red',fg='white').place(x=190,y=340)
        



    
#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window,
          #  image=bg
            ).place(x=0,y=0)
Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)


adnm=Label(window,text='enter admin name',
           bg='light blue',
           fg='purple',font=f).place(x=195,y=150)
adnm=Label(window,text='enter admin ID',
           bg='light blue',
           fg='black',font=f).place(x=210,y=250)
#adnm=Label(window,text='enter password:',bg='light blue',fg='black',font=f).place(x=130,y=380)
naame=StringVar()
admid=StringVar()
name=Entry(window,width=20,textvariable=naame).place(x=220,y=200)
name=Entry(window,width=20,textvariable=admid).place(x=220,y=300)

Button(window,text='enter',width=20,height=2,
       bg='green',fg='white',command=checking).place(x=207,y=370)




def adminlogin():
    adnm=input("Enter your name:")
    cntr=a.connect(user='root',password='YSshalini@09',host='localhost',database='project')
    c=cntr.cursor()
    c.execute("select * from admin")
    for i in c:
        if i[1]==adnm:
            adpas=input("Enter your password:")
            if i[2]==adpas:
                print('CORRECT PASSWORD!')
                
            if i[2]!=adpas:
                print('PASSWORD INCORRECT\n')
                adminlogin()
    c.execute("select * from admin")            
    for j in c:
        if i[1]!=adnm:
            print('ADMIN NOT FOUND\n')
            adminlogin()





Button(window,
       text='Go to main',
       command=main,
       fg='yellow',
       height=2,
       width=20,
       bg='black').place(x=10,y=550)
'''
Button(window,
       text='Back',
       fg='yellow',
       height=2,
       command=back,
       width=20,
       bg='black').place(x=200,y=550)'''

    



