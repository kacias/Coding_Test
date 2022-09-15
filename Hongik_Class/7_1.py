#1000번 문제 list 의 2개의 합으로 Target 만드는 문제
from typing import List

import time

'''
#Brute-Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''


'''
#검색 범위 축소 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):

            complement = target - n

            print("i:{}".format(i))
            print("n:{}".format(n))
            print("complement:{}".format(complement))


            if complement in nums[i + 1:]:

                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)  #검색 범위 축소
                #return nums.index(n), nums.index(complement)  #그냥 찾기 
'''




#딕셔너리: 해쉬 테이블로 더 빠르다.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        print("nums:{}".format(nums))
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        print("nums_map:{}".format(nums_map))
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]

'''

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        print("nums:{}".format(nums))

        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        print("nums_map:{}".format(nums_map))



        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
            #if target - num in nums_map:

                print ("i:{}".format(i))
                print ("num:{}".format(num))
                print ("nums_map[target - num]:{}".format(nums_map[target - num]))
                return nums.index(num), nums_map[target - num]


'''

'''
#for 문 통합 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 `for`문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

            #print(nums_map)

'''

#======================================================================
#가장 빠른거

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        #정렬을 하면 인덱스값이 흩뜨려짐.
        print(nums)

        #nums= sorted(nums)
        #print(nums)

        while not left == right:

            print("left:{}".format(left))
            print("right:{}".format(right))

            # 합이 타겟보다 작으면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right



if __name__ == "__main__":

    #==========

    a = Solution()
    b= a.twoSum([1,2,5,9], 14)
    print(b)



    #================================================
    #시간 체크
    '''
    s_time = time.time()

    a = Solution()
    c = [i for i in range(0, 3000)]
    b = a.twoSum(c, 4583)
    print(b)

    print("time elapsed:{}".format(time.time()-s_time))
    '''
    #=================================================



    #==========================
    #list.index(), 리스트를 검색해서 해당 값이 있으면 index값을 반환
    '''
    nums = [1,2,4]
    print(nums.index(4))
    print(nums.index(1))
    '''


    #==================
    #if i in List
    #리스트 안에 특정 값을 찾을 때
    '''
    nums = [1,2,3]
    a = 1
    if a in nums:
        print("find out:{}".format(1))
    '''



    #=======================
    #무난한 해법
    '''
    nums = [1,2,4]
    j = 5
    for idx, i in enumerate(nums):
        target = j - i

        if target in nums:
            print( nums.index(i), nums.index(target) )
    '''






