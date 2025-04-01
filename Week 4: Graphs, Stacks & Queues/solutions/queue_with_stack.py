class MyQueue:
    def __init__(self):
        self.stack1 = []  # Input stack
        self.stack2 = []  # Output stack

    def reverse_order(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            self.reverse_order()
        return self.stack2.pop() if self.stack2 else None

    def peek(self) -> int:
        if not self.stack2:
            self.reverse_order()
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Example usage:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# print(obj.peek())  # Should return 1
# print(obj.pop())   # Should return 1
# print(obj.empty()) # Should return False