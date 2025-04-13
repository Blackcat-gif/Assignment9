#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Book:
    id:int = 1
    title:str = "title"
    author:str = "author"
    publication_date:str = "01/01/2025"
    isbn:str = ""

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} ({self.publication_date})"
        
class Libary(Book):
    
    def add_book(self, book: Book):
        with closing(conn.cursor()) as c:
            sql = '''INSERT INTO Book (id, title, author, publication_date, isbn) VALUES (?, ?, ?, ?)'''
        c.execute(sql, (id, title, author, publication_date, isbn)) 
        conn.commit()


    def delete_book(self, book_id: int):
        with closing(conn.cursor()) as c: 
            sql = '''DELETE FROM Book WHERE ID = ?'''
        c.execute(sql, (id,)) 
        conn.commit()


x = Book()
x.__str__()


# In[ ]:




