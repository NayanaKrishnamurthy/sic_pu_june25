
class Student:
    def __init__(self, id=0, name='', marks=0.0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'ID= {self.id}, Name= {self.name}, Marks= {self.marks}'

class Node:
    def __init__(self, student=None):
        self.data = student
        self.link = None

    def create_student(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        return Student(id, name, marks)

class StackSLL:
    def __init__(self):
        self.top = None

    def insert(self):
        node = Node()
        student = node.create_student()
        node.data = student
        node.link = self.top
        self.top = node
        print("Student pushed into stack (SLL).\n")

    def delete(self):
        if self.top is None:
            print("Stack is empty\n")
            return
        print(f"Popped: {self.top.data}\n")
        self.top = self.top.link

    def display(self):
        if self.top is None:
            print("Stack is empty\n")
            return
        temp = self.top
        print("Stack contents:")
        while temp:
            print(temp.data)
            temp = temp.link
        print()

if __name__ == "__main__":
    s = StackSLL()
    while True:
        print("1. Push\n2. Pop\n3. Display\n4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            s.insert()
        elif ch == 2:
            s.delete()
        elif ch == 3:
            s.display()
        elif ch == 4:
            break
        else:
            print("Invalid choice\n")
