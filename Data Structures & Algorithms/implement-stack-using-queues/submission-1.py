from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue:
            self.queue2.append(self.queue.popleft())
        self.queue, self.queue2 = self.queue2, self.queue


    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]


    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()