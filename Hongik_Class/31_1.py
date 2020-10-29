#min heap https://coderkoo.tistory.com/10

import collections
import heapq
from typing import List

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = collections.Counter(nums)
        freqs_heap = []
        print("freqs:{}".format(freqs))

        #========================
        #파이썬에는 Max Heap이 없어서 이렇게 변형해서 사용함
        # 힙에 음수로 삽입
        for f in freqs:
            print("--------------------------------")
            print("f:{}".format(f))
            print("-freqs[f]:{}".format(-freqs[f]))
            heapq.heappush(freqs_heap, (-freqs[f], f))  #튜플 데이터를 heap에 삽입

            print("heapq:{}".format(freqs_heap))

        print("final heapq:{}".format(freqs_heap))
        topk = list()
        print("k:{}".format(k))

        #=============================================
        # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            d = heapq.heappop(freqs_heap)[1]
            print("popped data:{}".format(d))
            topk.append(d)
            #topk.append(heapq.heappop(freqs_heap)[1])

        return topk



if __name__=="__main__":

    #----------------------------
    #min heap test
    '''
    heap =[]

    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    heapq.heappush(heap, 7)
    heapq.heappush(heap, 9)

    #이진 트리 생성
    print(heap)
    '''

    #가장 작은 값을 삭제
    '''
    heapq.heappop(heap)
    print(heap)
    print(heap[0])
    '''


    '''
    l = [1,2,3,5,3,9]
    heapq.heapify(l)
    print(l)
    #-----------------------------
    '''

    #---------------------------------
    #우선 순위 min heap tree, 우선 순위를 튜플로 입력
    '''
    h = []
    heapq.heappush(h, (3, "Go to home"))
    heapq.heappush(h, (10, "Do not study"))
    heapq.heappush(h, (1, "Enjoy!"))
    heapq.heappush(h, (4, "Eat!"))
    heapq.heappush(h, (7, "Pray!"))

    print(h)

    k = len(h)

    #우선 순위대로 팝
    for _ in range(k):
        print("popped data:{}".format(heapq.heappop(h)))
    '''

    '''
    s= [1,2,2,2,2,9,9,9]
    a = Solution()
    print(a.topKFrequent(s, 2))
    '''
