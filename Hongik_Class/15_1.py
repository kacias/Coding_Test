# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        counter = 0
        while node:

            print("============================")
            print("iter:{}".format(counter))
            next, node.next = node.next, prev

            if next and node.next:
                print("next <- node.next:{}".format(next.val))
                print("node.next <- prev:{}".format(node.next.val))

            prev, node = node, next

            if prev and node:
                print("prev:{} <- node ".format(prev.val))
                print("node:{}".format(node.val))

            counter +=1


        return prev




'''
#디버깅
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(node: ListNode, prev: ListNode = None):
            print("====================================")

            if not node:
                return prev

            if node.next and prev:
                print("swapping between {} <--> {}".format(node.next.val, prev.val))
            next, node.next = node.next, prev


            return reverse(next, node)

        return reverse(head)
'''


#======================================
#메인 함수

if __name__=="__main__":

    #-----------------------
    #list 1 생성
    head = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)


    head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None


    #출력 확인
    q = []
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    print(q)

    #---------------------
    #뒤집기
    aa = Solution()
    aa.reverseList(head)

    #뒤집은 후 출력 확인
    q = []
    node = e  #위치가 뒤 바뀜
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)