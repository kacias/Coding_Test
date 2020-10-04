from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True



if __name__ == "__main__":

    #=========================
    #리스트 pop()
    f = [1, 2, 3, 6, 8, 10]
    print(f.pop(0))
    print(f.pop())


    '''
    #------------------------
    #list 기본 사용법 
    a = ListNode("a")
    b = ListNode("b")
    c = ListNode("a")
    e = ListNode("b")

    a.next = b
    b.next = c
    c.next = e
    c.next = None

    print(a.val)
    print(a.next.val)
    print(a.next.next.val)
    #------------------------
    #일반값을 넣으면 실패
    #d=10
    '''

    #----------------
    #노드 출력
    '''
    q = []
    node = a
    while node is not None:
        q.append(node.val)
        node = node.next
    print(q)
    '''


    '''
    aa = Solution()
    print(aa.isPalindrome(b))
    '''


