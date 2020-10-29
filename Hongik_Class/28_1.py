#https://www.fun-coding.org/Chapter09-hashtable.html
#https://m.blog.naver.com/PostView.nhn?blogId=mage7th&logNo=221494489570&proxyReferer=https:%2F%2Fwww.google.com%2F
#https://davinci-ai.tistory.com/19

import collections
import hashlib



# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1


    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next



if __name__=="__main__":

    #유니코드 문자열을 바이트로 인코딩
    '''
    t= b"Hi"
    print(t)
    print(hashlib.sha256(t).hexdigest())
    '''

    #DefaultDictionary
    '''
    ex1 = {'a': 1, 'b': 2}
    print(ex1)
    print(ex1['c'])
    '''

    #딕셔너리에 없는 값 조회 시 에러
    '''
    n_dict = dict()
    print(n_dict["a"])
    '''

    #매번 Setdefault로 일일히 초기값을 넣어주어야 함.
    '''
    n_dict = dict()
    n_dict.setdefault("a", 0)
    print(n_dict["a"])
    '''

    #default Dictionary는 초기값을 기본 장착한 딕셔너리

    '''
    d_dict = collections.defaultdict(int)
    print(d_dict["a"])
    d_dict["b"] += 10
    print(d_dict)
    '''

    #===============================================
    #default Dictionary에 ListNode를 추가
    #문제 해석용 코드
    '''
    listnode_dict = collections.defaultdict(ListNode)
    a_node = ListNode(10, 99)
    b_node = ListNode(10, 199)
    c_node = ListNode(20, 299)

    #아래와 같은 구조가 아님
    #listnode_dict[a_node.key] = a_node.value
    #listnode_dict[b_node.key] = b_node.value

    #해쉬함수로 변환된 값을 인덱스로 사용하는 구조 
    listnode_dict["hash_0"] = a_node
    listnode_dict["hash_0"] = b_node #이럴 경우 리스트를 연결함 a_node.next = b_node
    listnode_dict["hash_1"] = c_node

    print(listnode_dict)
    '''
    #==================================================



    a = MyHashMap()
    a.put(10,1)
    a.put(20,25)
    a.put(45,15)

    print(a.get(10))
    print(a.get(20))
    a.remove(10)
    print(a.get(10))

