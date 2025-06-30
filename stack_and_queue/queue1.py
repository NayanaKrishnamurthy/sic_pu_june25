import sys as s

queue= []

def push_rear():
    item = input("Enter item to push (rear): ")
    queue.append(item)
    print(f"'{item}' pushed to the queue.")

def pop_front():
    if queue:
        item = queue.pop(0)
        print(f"Popped item from front (top): {item}")
    else:
        print("Queue is empty.")

def display():
    if queue:
        print("Queue :")
        print(queue[:])
            
    else:
        print("Queue is empty.")

def exit_program():
    s.exit("End of program.")



def menu(choice):
    match(choice):
        case 1:
            push_rear()
        case 2:
           pop_front()
        case 3:
           display()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print("1:Push 2:Pop 3:Display 4:Exit")
    choice = int(input("Your choice: "))
    menu(choice)
    