
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 단순연결 리스트
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    #새로운 head 삽입 함수
    def InsertFirst(self, data):
        new_node = Node(data)
        temp_node = self.head   #기존 헤드 잠시 보관
        self.head = new_node    #헤드를 새로운 헤드로 변경
        self.head.next = temp_node    #새로 새성된 헤드의 링크를 기존 헤드의 링크로 변경
        self.list_size += 1

    #출력 함수
    def __str__(self):
        print_list = '['
        node = self.head #1
        while True: #2
            print_list += str(node.data) #4하고 싶은 거
            if node.next == None: #3탈출 조건
                break
            node = node.next   #5이동
            print_list += ", "
        print_list += "]"
        return print_list


    #맨 마지막에 노드 추가
    def InsertLast(self, data):
        node = self.head

        #끝까지 이동한 다음
        while True:
            if node.next == None:
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1


    #링크드 리스트 인덱스를 기준으로 검색 함수
    def SelectNode(self, num):
        if self.list_size < num:
            return

        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1

        #return node.data #값이 궁금하다면
        return node

    #중간 삽입 함수
    def InsertMiddle(self, num, data):

        if self.head.next == None:
            InsertLast(data)
            return

        node = self.SelectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1


    #헤더 삭제 함수
    def DeleteHead(self):
        node = self.head
        self.head = node.next
        self.list_size -= 1
        del node

    #특정 위치 노드 삭제
    def DeleteNode(self, num):
        if self.list_size < 1:
            return #underflow
        elif self.list_size < num:
            return #overflow

        if num == 0:
            self.DeleteHead()
            return

        node = self.SelectNode(num-1)

        del_node = node.next
        node.next = node.next.next

        self.list_size -= 1
        del del_node


if __name__ =="__main__":

    a = SingleLinkedList(100)
    a.InsertFirst(200)
    a.InsertFirst(300)
    print(a)

    a.InsertLast(999)
    a.InsertLast(9999)

    print(a)

    c= a.SelectNode(3)
    print(c.data)
    print(a.list_size)

    a.InsertMiddle(2, 888)
    print(a)

    a.DeleteHead()
    print(a)

    a.DeleteNode(3)
    print(a)

    '''
    a = Node(100)
    b = Node(200)
    c = Node(300)

    a.next = b
    b.next = c
    head = a

    print(a.data)
    print(b.data)
    print(a.next)
    print(a.next.data)
    print(head.next.next.data)
    '''



    #-----------------------
    #연결 리스트 --> 파이썬 리스트
    '''
    q = []
    node = head
    while node is not None:
        q.append(node.data)
        node = node.next
    print(q)
    '''
    #-----------------------


