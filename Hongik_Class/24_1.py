#https://www.daleseo.com/python-queue/
#https://monsieursongsong.tistory.com/5

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


if __name__=="__main__":

    a = MyQueue()
    a.push(10)
    a.push(20)
    b = a.pop()
    print(b)

    print(a)
    a.peek()
    print(a)