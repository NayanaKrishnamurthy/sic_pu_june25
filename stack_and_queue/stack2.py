import sys as s

stack = []

def push_front():
    item = input("Enter item to push (front): ")
    stack.insert(0,item)
    print(f"'{item}' pushed to the stack.")

def pop_front():
    if stack:
        item = stack.pop(0)
        print(f"Popped item from stack: {item}")
    else:
        print("Stack is empty.")

def display_front():
    if stack:
        print("Stack (Top to Bottom):")
        print(stack[:])
            
    else:
        print("Stack is empty.")

def exit_program():
    s.exit("End of program.")



def menu(choice):
    match(choice):
        case 1:
           push_front()
        case 2:
           pop_front()
        case 3:
           display_front()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print("1:Push 2:Pop 3:Display 4:Exit")
    choice = int(input("Your choice: "))
    menu(choice)