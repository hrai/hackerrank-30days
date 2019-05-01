from collections import deque

class Solution(object):
    stack=[]
    queue=deque([])

    """docstring for Solution"""

    def pushCharacter(self, ch):
        self.stack.append(ch)
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()
