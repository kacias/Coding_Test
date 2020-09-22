from typing import List


#두개의 포인터를 이동
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        print(s)
'''

#함수 사용
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

        print(s)


if __name__ == "__main__":
    #a = [1, 2, 4]
    #print(a.pop())


    a = Solution()
    a.reverseString([1,2,3,4])




