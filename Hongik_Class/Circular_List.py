#원형 리스트
#https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8
#위의 코드 중 오류 수정 버전
#Node는 [ Data | Next ]

#                            <Head>                                 <Tail>
# CircleLinkedList는    [ Data | Next ] --> [ Data | Next ] --> [ Data | Next ]
#                          |                                             |
#                          -----------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = None
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            if node:
                print_list += str(node.data)
            if node == self.tail:
            # 단순 연결 리스트와 달리
            # 노드가 테일 노드면 끝난다
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    #헤드 추가 함수
    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail == None:    #테일 추가
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node  #테일 추가
        self.list_size += 1

    #중간에 넣는 함수는 동일
    def insertMiddle(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    #맨 마지막에 넘느 함수는 tail 처리 필요
    def insertLast(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            print("Overflow")
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size < num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)

    def get_head_tail(self):
        return self.head.data, self.tail.data


#메인 함수
if __name__ == "__main__":

    a = CircleLinkedList(100)
    print(a.size())


    a.insertFirst(999)
    a.insertFirst(9990)


    a.insertLast(77)

    a.insertMiddle(2, 500)

    b, c = a.get_head_tail()

    print("head:{} tail:{}".format(b, c))


    print(a)