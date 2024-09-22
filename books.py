import mysql.connector as a
cntr=a.connect(user='root',password='YSshalini@09',host='localhost',database='project')
c=cntr.cursor()
f=('bahnschrift',17)


from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")

background_label = Label(window)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import view


#Label(window,text='',bg='light blue',heigh=50,width=100).place(x=0,y=0)



c.execute("SELECT bookID,name,author FROM books")
i=1
Label(window,text='Book id',font=f,width=40,height=2,bg='green',fg='white').grid(row=0,column=0)
Label(window,text='Book name',font=f,width=40,height=2,bg='green',fg='white').grid(row=0,column=1)
Label(window,text='Authors',font=f,width=40,height=2,bg='green',fg='white').grid(row=0,column=2)

for stu in c:
    ii=0
    for j in stu:
        Label(window,text=j,
                  width=40,font=f,height=2,bg='light blue',fg='blue').grid(row=i,column=ii)
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
