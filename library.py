from datetime import datetime, timedelta
class libraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None
        
    def borrow(self, days= 14):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.due_date = datetime.now() + timedelta(days=days)
            print(f'"{self.title}" borrowed. Due date: {self.due_date.strftime("%Y-%m-%d")}')
        else:
            print(f'"{self.title}" is already borrowed')
    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.due_date = None
            print(f'"{self.title}" return suuccessfully.')
        else:
            print(f'"{self.title}" was not borrowed.')
    
    def display_info(self):
        status = "Availabel" if not self.is_borrowed else f"Borrowed, Due: {self.due_date.strftime('%Y-%m-%d')}"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")
    
# Book 
class Book(libraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author) 
        self.genre = genre
        
    def display_info(self): #
        super().display_info()
        print(f'Genre: {self.genre}')
        
# Magazin
class Magazine(libraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
        
    def display_info(self):
        super().display_info()
        print(f'Issue Number: {self.issue_number}')
        