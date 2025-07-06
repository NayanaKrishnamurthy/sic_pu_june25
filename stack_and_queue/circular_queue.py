
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def insert(self, data):
        
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full (Overflow)")
            return

        if self.front == -1:  
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print("Inserted:", data)

    def delete(self):
        if self.front == -1:
            print("Queue is Empty (Underflow)")
            return

        print("Deleted:", self.queue[self.front])

        if self.front == self.rear:
            self.front = self.rear = -1  
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Circular Queue Contents:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


if __name__ == "__main__":
    cq = CircularQueue(5)
    while True:
        print("\n1. Insert\n2. Delete\n3. Display\n4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            val = input("Enter value to insert: ")
            cq.insert(val)
        elif ch == 2:
            cq.delete()
        elif ch == 3:
            cq.display()
        elif ch == 4:
            break
        else:
            print("Invalid choice.")
