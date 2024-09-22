from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("600x600")

f=('bahnschrift',10)
#bg=PhotoImage(file='C:/comp project-library/BGs/cross books.GIF')

label=Label(window,
           # image=bg
            ).place(x=0,y=0)
'''
bgi=PhotoImage(file='C:/comp project-library/BGs/big background - Copy3.gif')
label=Label(window,
            image=bgi
            ).place(x=50,y=50)

'''

def allbook():
    window.destroy()
    import books-1
def tomain():
    window.destroy()
    import projectmain-1
def bkid():
    window.destroy()
    import searchbookid
def bookname():
    window.destroy()
    import searchnames
def author():
    window.destroy()
    import searchauthor    


Label(window,
      text='',
      bg='light blue',
      height=20,
      width=50).place(x=110,y=140)

Button(window,
       text='view all book',
       height=2,
       font=f,
       command=allbook,
       width=30).place(x=180,y=180)

Button(window,
       text='Find using book name',
       height=2,
       font=f,
       command=bookname,
       width=30).place(x=180,y=240)

Button(window,
       text='Find using author name',
       height=2,
       font=f,
       command=author,
       width=30).place(x=180,y=300)

Button(window,
       text='Find using book id',
       height=2,
       font=f,
       width=30,
       command=bkid).place(x=180,y=360)
Button(window,
       text='Back',
       fg='yellow',
       height=2,
       command=tomain,
       width=20,
       bg='black').place(x=10,y=550)


