from datetime import datetime, timedelta
class library:
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
            