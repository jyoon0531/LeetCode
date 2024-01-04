class Node:
    # 연결리스트에서의 노드, item은 데이터를 저장, next는 다음 노드를 참조
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    # push, pop, is_empty
    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next
        return node.item

class Solution:
    def isValid(self, s: str) -> bool:
        opener = "({["
        stack = Stack()

        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in opener:
                stack.push(char)
            elif char in pair:
                if stack.is_empty() or stack.pop() != pair[char]:
                    return False

        return stack.is_empty()           

        

