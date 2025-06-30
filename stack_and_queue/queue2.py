import sys as s

queue= []

def push_front():
    item = input("Enter item to push (front): ")
    queue.insert(0,item)
    print(f"'{item}' pushed to the queue.")

def pop_rear():
    if queue:
        item = queue.pop()
        print(f"Popped item from rear : {item}")
    else:
        print("Queue is empty.")

def display():
    if queue:
        print("Queue :")
        print(queue[::-1])
            
    else:
        print("Queue is empty.")

def exit_program():
    s.exit("End of program.")



def menu(choice):
    match(choice):
        case 1:
            push_front()
        case 2:
           pop_rear()
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
    