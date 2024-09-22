from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")

f=('bahnschrift',10)
bg = PhotoImage(file='C:/Users/DELL/Downloads/lib manag sys/lib1-pic.gif')
background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def allbook():
    window.destroy()
    import books
def tomain():
    window.destroy()
    import projectmain
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
      width=50).place(x=600,y=140)

Button(window,
       text='VIEW ALL BOOK',
       height=2,
       font=f,
       command=allbook,
       width=30).place(x=670,y=180)

Button(window,
       text='FIND USING BOOK NAME',
       height=2,
       font=f,
       command=bookname,
       width=30).place(x=670,y=240)

Button(window,
       text='FIND USING AUTHOR NAME',
       height=2,
       font=f,
       command=author,
       width=30).place(x=670,y=300)

Button(window,
       text='FIND USING BOOK ID',
       height=2,
       font=f,
       width=30,
       command=bkid).place(x=670,y=360)
Button(window,
       text='BACK',
      # fg='yellow',
       height=2,
       command=tomain,
       width=20,
      # bg='black'
       ).place(x=690,y=550)


