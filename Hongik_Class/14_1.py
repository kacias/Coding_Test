# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
'''


#================
#debugging
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print("================================")
        if (not l1) or (l2 and l1.val > l2.val):
            print("l1 <-> l2 swaping")
            if l1:
                print("current_l1:{}".format(l1.val))
            if l2:
                print("current_l2:{}".format(l2.val))
            l1, l2 = l2, l1

        if l1:
            print("go deeper")
            print("current_l1:{}".format(l1.val))
            if l2:
                print("current_l2:{}".format(l2.val))

            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

    def test(self, l1):
        if l1:
            print("not l1")
            print(l1.val)


if __name__=="__main__":

    '''
    a = ListNode(1)
    aa = Solution()
    aa.test(a)
    '''


    #-----------------------
    #list 1 생성
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)

    a.next = b
    b.next = c
    c.next = None

    #출력 확인
    q = []
    node = a
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)

    #-----------------------
    #list 2 생성
    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)

    d.next = e
    e.next = f
    f.next = None

    #출력 확인
    q = []
    node = d
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)


    #----------------------------------
    #main
    aa = Solution()
    result = aa.mergeTwoLists(a, d)

    q = []
    node = result
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)
    #===================================


