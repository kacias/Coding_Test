#이중 링크드 리스트
#https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8
#위의 코드 중 오류 수정 버전
#Node는 [ Prev | Data | Next ]

#                            <Head>
# DualLinkedList    [ Prev | Data | Next ] --> [ Prev | Data | Next ] --> [ Prev | Data | Next ]



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class DualLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == self.head:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        if not self.head.prev == None:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
        if not self.head.next == None:
            new_node.next = self.head.next
        self.head.prev = new_node
        self.head = new_node
        self.list_size += 1

    def insertMiddleAfter(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.list_size += 1

    def insertMiddleBefore(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.list_size += 1

    def insertLast(self, data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head

        if not self.head.prev == None:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow
        count = 0
        node = self.head
        if int(self.list_size/2) > num:
            while count < num:
                node = node.next
                count += 1
        else:
            repeat = self.list_size - num
            while count < repeat:
                node = node.prev
                count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num)
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def deleteHead(self):
        node = self.head
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)


#메인 함수
if __name__ == "__main__":


    a = DualLinkedList(100)
    print(a.size())

    a.insertLast(2342)
    a.insertLast(777)
    a.insertMiddleAfter(1, 300)
    a.insertMiddleAfter(2, 400)

    print(a.size())
    print(a)

    a.selectNode(2)

    #basic
    #a = DualLinkedList(100)
    #a.insertFirst(200)
    #print(a)
