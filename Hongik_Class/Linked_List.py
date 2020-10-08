#https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#단순연결 리스트
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





    def __str__(self):
        print_list = '['
        node = self.head
        while True:
            print_list += str(node.data)
            if node.next == None:
                break
            node = node.next
            print_list += ", "
        print_list += "]"
        return print_list



#메인 함수
if __name__ == "__main__":

    #basic
    '''
    head = Node(0)
    node_1 = Node(1)
    head.next = node_1

    print(head.data)
    print(head.next.data)
    '''

    #single liked list
    a = SingleLinkedList(100)

    a.InsertLast(200)
    a.InsertLast(300)
    print(a)


    #헤더 교체
    a.InsertFirst(1000)
    a.InsertFirst(3000)
    print(a)


    a.InsertMiddle(1, 999)
    print(a)

    #맨 마지막 노드 추가
    #a.InsertLast(1000)


    #print(a.SelectNode(2))
