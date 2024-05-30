class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)    
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"the library has {self.noBooks} books. the books are") 
        for book in self.books:
            print(book)
            


l1 = Library()        
l1.addBook("Rehan Python1")
l1.addBook("Rehan Python2")
l1.addBook("Rehan Python3")
l1.addBook("Rehan Python4")
l1.addBook("Rehan Python5")
l1.addBook("Rehan Python6")
l1.showInfo()