class Library:
    def __init__(self, id, publisher, author, title):
        self.id = id
        self.publisher = publisher
        self.author = author
        self.title = title
        self.no_of_books = 5
        self.charge = 0.0
    
    def read(self):
        print(f"{self.id} has {self.title} and {self.author}")


    def compute(self,no_of_books):
        self.no_of_books = no_books
        self.charge = no_books * 1.5
        print(f"{self.charge}$ is total charge for renting books for read")

def main():
    l1 = Library("abc1","Rich dad","Harry","potter")
    l1.read()
    l1.compute(5)

if __name__== "main":
    main()