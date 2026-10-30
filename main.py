from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def test_stack(stack, name):
    print(f"\n--- Testing {name} ---")
    while True:
        print("\n1. Push\n2. Pop\n3. Peek\n4. Check Empty\n5. Exit to Main Menu")
        choice = input("Enter choice: ")
        try:
            if choice == '1':
                val = input("Enter value to push: ")
                stack.push(val)
                print(f"Pushed {val} successfully.")
            elif choice == '2':
                print(f"Popped value: {stack.pop()}")
            elif choice == '3':
                print(f"Top value: {stack.peek()}")
            elif choice == '4':
                print(f"Is empty? {stack.is_empty()}")
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

def test_queue(queue, name):
    print(f"\n--- Testing {name} ---")
    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Peek Front\n4. Check Empty\n5. Exit to Main Menu")
        choice = input("Enter choice: ")
        try:
            if choice == '1':
                val = input("Enter value to enqueue: ")
                queue.enqueue(val)
                print(f"Enqueued {val} successfully.")
            elif choice == '2':
                print(f"Dequeued value: {queue.dequeue()}")
            elif choice == '3':
                print(f"Front value: {queue.peek_front()}")
            elif choice == '4':
                print(f"Is empty? {queue.is_empty()}")
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    while True:
        print("\n=== Data Structures Laboratory: Stacks & Queues ===")
        print("1. Array Stack")
        print("2. Linked List Stack")
        print("3. Circular Array Queue")
        print("4. Linked List Queue")
        print("5. Exit")
        
        choice = input("Select implementation: ")
        if choice == '1':
            cap = int(input("Enter stack capacity: "))
            s = ArrayStack(cap)
            test_stack(s, "Array Stack")
        elif choice == '2':
            s = LinkedStack()
            test_stack(s, "Linked Stack")
        elif choice == '3':
            cap = int(input("Enter queue capacity: "))
            q = ArrayQueue(cap)
            test_queue(q, "Circular Array Queue")
        elif choice == '4':
            q = LinkedQueue()
            test_queue(q, "Linked Queue")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()