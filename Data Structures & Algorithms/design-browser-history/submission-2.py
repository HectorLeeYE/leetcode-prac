class Node:
    def __init__(self, url="", next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url, prev=self.curr)
        self.curr.next = new_node

        # Update current pointer to new_node
        self.curr = new_node


    def back(self, steps: int) -> str:
        if steps == 0:
            return self.curr.url


        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1      # Move backwards and decrement 
        
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        
        if steps == 0:
            return self.curr.url 
        
        while steps > 0 and self.curr.next: 
            self.curr = self.curr.next
            steps -= 1

        return self.curr.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)