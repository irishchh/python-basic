class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def book_title(self):
        print(f"{self.title} is the author of {self.author}")


class Fiction(Book):
    def __init__(self, author, title, publisher):
        super().__init__(author, title)
        self.publisher = publisher

    def book_info(self):
        print(f"{self.title} is authored by {self.author} and published by {self.publisher}")
        super().book_info()

class Fiction(Book):
    def __init__(self,author,title,publisher):
        super().__init__(author,title)
        self.publisher = publisher
    def book_info(self):
        super().book_info()




def main():
    print("Derived class")
    silva_book = Fiction("Daniel Sliva", "Prince of fire", "Berkery")
    silva_book.book_info()
    silva_book.invoke()


print("-"*20)
print("Base class")

if __name__ == "__main__":
    main()


    

# user define data type 
#in-built define data type