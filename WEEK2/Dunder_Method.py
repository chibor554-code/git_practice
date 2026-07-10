class Book: 
    def __init__(self, title, author, pages): 
        self.title  = title 
        self.author = author 
        self.pages  = pages 
        
    def __str__(self): 
        """User-friendly string — for print()""" 
        return f"'{self.title}' by {self.author}" 
    
    def __repr__(self): 
        """Developer string — for repr() and debugging""" 
        return f"Book('{self.title}', '{self.author}', {self.pages})" 
    
    def __len__(self): 
        """Returns number of pages when len() is called""" 
        return self.pages 
    
    def __eq__(self, other): 
        """Two books are equal if same title and author""" 
        if not isinstance(other, Book): 
            return False 
        return self.title == other.title and self.author == other.author 
    
    def __lt__(self, other): 
        """Compare by page count — enables sorting""" 
        return self.pages < other.pages 
    
b1 = Book("Python Crash Course", "Eric Matthes", 544) 
b2 = Book("Clean Code", "Robert Martin", 464) 
print(b1)            # 'Python Crash Course' by Eric Matthes 
print(repr(b1))      # Book('Python Crash Course', 'Eric Matthes', 544) 
print(len(b1))       # 544 
print(b1 == b2)      # False 
print(b1 < b2)       # False (544 < 464 is False) 
books = [b1, b2] 
books.sort()         # works because __lt__ is defined 