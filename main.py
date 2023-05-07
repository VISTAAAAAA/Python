import sqlite3
from EMP import books
conn = sqlite3.connect('LIBRARY.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS books(
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    code INTEGER NOT NULL,
    copies INTEGER NOT NULL)""")

def create_lib(lib):
    with conn:
        c.execute("INSERT INTO books VALUES (:title, :author, :code, :copies)",
                  {'title': lib.title, 'author': lib.author, 'code': lib.code, 'copies': lib.copies})

def read_lib(code):
    c.execute("SELECT * FROM books WHERE code = :code", {'code': code})
    rec = c.fetchall()
    for i in rec:
        print("Title: ", i[0])
        print("Author: ", i[1])
        print("ISBN: ", i[2])
        print("Number of Copies: ", i[3])


def update_lib(code, num):
    with conn:
        if num == 1:
            new1 = input("Input new Title: ")
            c.execute("""UPDATE books SET title = :title WHERE code = :code""", {'title': new1, 'code': code})
        if num == 2:
            new2 = input("Input new Author: ")
            c.execute("""UPDATE books SET author = :author WHERE code = :code""", {'author': new2, 'code': code})
        if num == 3:
            new3 = input("Input new number of copies: ")
            c.execute("""UPDATE books SET copies = :copies WHERE code = :code""", {'copies': new3, 'code': code})

def remove_lib(code):
    with conn:
        c.execute("DELETE FROM books WHERE code = :code", {'code': code})

while True:
    print("===================================================================")
    print("chose your desired operation\n(a)dd book\n(s)earch for book\n(u)pdate book\n(d)elete book\n(q)uit")
    a1 = input("Input the letter of your desired operation: ")
    if a1.lower() == 'a':
        name = input("Input the Title of the Book: ")
        author = input("Input the Author of the Book: ")
        code = int(input("Input the ISBN of the Book: "))
        copies = int(input("Input the number of copies of the Book: "))
        user = books(name, author, code, copies)
        create_lib(user)
    if a1.lower() == 's':
        a = input("Enter book's ISBN: ")
        print(read_lib(a))
    if a1.lower() == 'u':
        a = input("Enter book's ISBN: ")
        print("1. Name\n2. Author\n3. Number of copies")
        b = int(input("Enter the number of information that you want to update: "))
        update_lib(a, b)
    if a1.lower() == 'd':
        a = input("Input the ISBN that you wanted to delete: ")
        remove_lib(a)
    if a1.lower() == 'q':
        break
