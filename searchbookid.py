from tkinter import *
import mysql.connector

window = Tk()
window.title("LIBRARY MANAGEMENT PYTHON PROGRAM")
window.geometry("1918x1080")
f = ('bahnschrift', 15)

def main():
    window.destroy()
    import projectmain

def back():
    window.destroy()
    import view

def search_book():
    book_name = entry_book_name.get()
    entry_book_name.delete(0, 'end')  # Clear the entry field after taking input
    
    # Connect to MySQL database
    try:
        conn = mysql.connector.connect(user='root', password='YSshalini@09', host='localhost', database='project')
        cursor = conn.cursor()
        
        # Execute the query to search for the book
        cursor.execute("SELECT * FROM books WHERE bookID = %s", (book_name,))
        book_details = cursor.fetchone()  # Fetch the first result
        
        if book_details:
            # If book found, display its details
            book_info_label.config(text=f"Book ID: {book_details[7]}\nName: {book_details[0]}\nAuthor: {book_details[1]}")
        else:
            # If book not found, display "No record found"
            book_info_label.config(text="No record found")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

# Labels and Entry for book name
Label(window, text='', bg='light blue', height=20, width=200).place(x=60, y=140)
Label(window, text='ENTER BOOK ID', font=f).place(x=610, y=200)
Label(window, text=':', font=f, bg='light blue').place(x=600, y=242)
entry_book_name = Entry(window, width=20)
entry_book_name.place(x=630, y=250)

# Button for searching book
search_button = Button(window, text='Search', fg='yellow', height=2, command=search_book, width=20, bg='black')
search_button.place(x=650, y=350)

# Label for displaying book details or "No record found"
book_info_label = Label(window, text='', font=f, bg='light blue')
book_info_label.place(x=210, y=300)

# Buttons for navigation
Button(window, text='Go to main', command=main, fg='yellow', height=2, width=20, bg='black').place(x=10, y=550)
Button(window, text='Back', fg='yellow', height=2, command=back, width=20, bg='black').place(x=200, y=550)

window.mainloop()
