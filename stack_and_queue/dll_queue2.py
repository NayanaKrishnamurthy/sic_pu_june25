
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

class QueueDLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self):
        node = DNode()
        student = node.create_student()
        node.data = student
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        print("Student inserted into queue (DLL).\n")

    def delete(self):
        if self.front is None:
            print("Queue is empty\n")
            return
        print(f"Deleted: {self.front.data}\n")
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty\n")
            return
        temp = self.front
        print("Queue contents:")
        while temp:
            print(temp.data)
            temp = temp.next
        print()

# Driver code
if __name__ == "__main__":
    q = QueueDLL()
    while True:
        print("1. Insert\n2. Delete\n3. Display\n4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            q.insert()
        elif ch == 2:
            q.delete()
        elif ch == 3:
            q.display()
        elif ch == 4:
            break
        else:
            print("Invalid choice\n")
