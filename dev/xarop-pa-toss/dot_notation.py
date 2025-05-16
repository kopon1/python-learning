x = 'this is a word'
number = 10
some_float = 4.5

class Book:
    def __init__(self, title, author):
        print(title)
        self.this_title = "The title is " + title
        print(self.this_title)
        print(author)
        self.this_author = "The author is " + author
        print(self.this_author)
        print(" ")
    
    def print_title_to_upper(self):
        return self.this_title.upper()
    
    def separate_title_words(self):
        return self.this_title.split(" ")
        
book_one = Book("The Hobbit", "J. R. R. Tolkien")
book_two = Book("The Catcher in the Rye", "J. D. Salinger")

print(book_one.this_author)
print(book_one.this_title)