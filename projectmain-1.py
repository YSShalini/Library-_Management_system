from tkinter import *
window=Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("600x600")



#bg=PhotoImage(file='C:/Users/DELL/Downloads/lib manag sys/background.JPG')

label=Label(window,
            #image=bg
            ).place(x=0,y=0)

Label(window,
      text="LIBRARY MANAGEMENT",
      bg='light blue',
      fg='black',
      height=2,
      width=30).place(x=180,y=20)

def view():
    window.destroy()
    import view
def addbook():
    window.destroy()
    import addbooks
def borr():
    window.destroy()
    import borrowedbk
def card():
    window.destroy()
    import carddetail


Button(window,
       text='View book',
       bg="red",
       fg="yellow",
       height=1,
       width=20,
       command=view).place(x=210,y=200)

Button(window,
       text="Add book",
       bg='blue',
       fg='white',
       command=addbook,
       height=1,
       width=20).place(x=210,y=250)

Button(window,
       text="Borrowed book details",
       bg='green',
       fg='white',command=borr,
       height=1,
       width=20).place(x=210,y=300)

Button(window,
       text="Reader's card details",
       bg='black',
       fg='yellow',
       height=1,command=card,
       width=20).place(x=210,y=350)
