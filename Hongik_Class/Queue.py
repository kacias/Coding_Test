
#===============================
#1) 리스트 사용
queue = [4, 5, 6]

#오른쪽 (Back) append = Enqueue
queue.append(7)
queue.append(8)

#왼쪽 (Front) pop = Dequeue
print(queue.pop(0))
print(queue.pop(0))

#추가 Back Popup
print(queue.pop())
print(queue.pop())


#=============================
#2) queue 사용
#데이터 추가/삭제는 O(1), 데이터 접근은 O(N)
#스레드 프로그래밍용

from queue import Queue

queue1 = Queue()

queue1.put(100)
queue1.put(200)
print(queue1.get())
print(queue1.get())




#=============================
#3) collections deque 사용
#double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료 구조
#데이터 추가/삭제는 O(1), 데이터 접근은 O(N)
#popleft()와 appendleft(x)메서드는 모두 O(1) -->  list의 pop(0)와 insert(0, x) 대비 성능 상에 큰 이점

from collections import deque

queue2 = deque([1,2,3,4])

#Enqueue
queue2.append(10)
queue2.append(20)
print(queue2)

#Dequeue
print(queue2.popleft())
print(queue2.popleft())


#Front에 추가
queue2.appendleft(100)
queue2.appendleft(200)
print(queue2)

#Back 삭제
print(queue2.pop())


#=====================================
#Queue 클래스 List로 구현

class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def enqueue(self, n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(7)


    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())


    a.printQueue()


