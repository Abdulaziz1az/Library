from library import Book
from library import Magazine

def main():
    items = [
        Book("1984", "George Orwell", "Dystopian"),
        Magazine("National Geographic", "Various", "March 2025")
    ]
    
    while True:
        print("\nLibrary System")
        print("1. Display items")
        print("2. Borrow an item")
        print("3. Return an items")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            for i, item in enumerate(items, 1):
                print(f"{i}.", end=" ")
                item.display_info()
                
        elif choice == "2":
            item_num = int(input("Enter item number to borrow: ")) - 1
            if 0 <= item_num <len(items):
                items[item_num].borrow()
            else:
                print("Invalid item number")
        
        elif choice == "3":
            item_num = int(input("Enter item number to return: ")) - 1
            if 0 <= item_num < len(items):
                items[item_num].return_item()
            else:
                print("Invalid item number")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()
        