import sys as s

stack = []

def push_rear():
    item = input("Enter item to push (rear): ")
    stack.append(item)
    print(f"'{item}' pushed to the rear (top) of stack.")

def pop_rear():
    if stack:
        item = stack.pop()
        print(f"Popped item from rear (top): {item}")
    else:
        print("Stack is empty.")

def display_rear():
    if stack:
        print("Stack (Top to Bottom):")
        print(stack[::-1])
            
    else:
        print("Stack is empty.")

def exit_program():
    s.exit("End of program.")



def menu(choice):
    match(choice):
        case 1:
            push_rear()
        case 2:
           pop_rear()
        case 3:
           display_rear()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print("\n[Rear-based Stack] 1:Push 2:Pop 3:Display 4:Exit")
    choice = int(input("Your choice: "))
    menu(choice)