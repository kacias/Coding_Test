# python list 활용한 Stack 구현
# Linked List를 활용하여 Stack 구현도 가능

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

if __name__ == "__main__":

    '''
    a = [1,2,3]
    print(a.pop())
    print(a[-1])
    print(a)
    '''

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.peek())
    print(s.pop())
    print(s.pop())




