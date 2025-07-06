
class Student:
    def __init__(self, id=0, name='', marks=0.0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'ID= {self.id}, Name= {self.name}, Marks= {self.marks}'

class DNode:
    def __init__(self, student=None):
        self.data = student
        self.prev = None
        self.next = None

    def create_student(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        return Student(id, name, marks)

class StackDLL:
    def __init__(self):
        self.rear = None

    def insert(self):
        node = DNode()
        student = node.create_student()
        node.data = student
        if self.rear is None:
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        print("Student pushed into stack (DLL).\n")

    def delete(self):
        if self.rear is None:
            print("Stack is empty\n")
            return
        print(f"Popped: {self.rear.data}\n")
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None

    def display(self):
        if self.rear is None:
            print("Stack is empty\n")
            return
        temp = self.rear
        print("Stack contents (top to bottom):")
        while temp:
            print(temp.data)
            temp = temp.prev
        print()

# Driver code
if __name__ == "__main__":
    s = StackDLL()
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
