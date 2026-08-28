class MyStack:

    def __init__(self):
        self.queue_1 = []
        

    def push(self, x: int) -> None:
        queue = self.queue_1
        queue.append(x)

    def pop(self) -> int:
        queue = self.queue_1
        return queue.pop()


    def top(self) -> int:
        queue = self.queue_1
        return queue[len(queue)-1]


    def empty(self) -> bool:
        queue = self.queue_1
        if len(queue) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()