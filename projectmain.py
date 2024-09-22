from tkinter import *

window = Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")

bg = PhotoImage(file='C:/Users/DELL/Downloads/lib manag sys/lib1-pic.gif')
#"C:\Users\DELL\Downloads\lib manag sys\library.jpeg"
# Assigning the background image to a variable
background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(window,
     text="LIBRARY MANAGEMENT",
                    bg='light blue',
                    fg='black',
                    font=("Helvetica", 18, "bold"),  # Larger font size and bold
                    padx=10,  # Padding around the text
                    pady=10,  # Padding around the text
                    width=25).place(x=550, y=70)

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
       text='VIEW BOOK',
       bg='black',
       fg='yellow',
       font=("Helvetica", 10, "bold"),  # Larger font size and bold
                    padx=4,  # Padding around the text
                    pady=5,  # Padding around the text
                    width=25,
       command=view).place(x=650, y=200)

Button(window,
       text="ADD BOOK",
       bg='black',
       fg='yellow',
       font=("Helvetica", 10, "bold"),  # Larger font size and bold
                    padx=4,  # Padding around the text
                    pady=5,  # Padding around the text
                    width=25).place(x=650, y=300)

Button(window,
       text="BORROWED BOOK DETAILS",
      bg='black',
       fg='yellow',
       font=("Helvetica", 10, "bold"),  # Larger font size and bold
                    padx=4,  # Padding around the text
                    pady=5,  # Padding around the text
                    width=25).place(x=650, y=400)

Button(window,
       text="READER'S CARD DETAILS",
       bg='black',
       fg='yellow',
       font=("Helvetica", 10, "bold"),  # Larger font size and bold
                    padx=4,  # Padding around the text
                    pady=5,  # Padding around the text
                    width=25).place(x=650, y=500)

window.mainloop()
