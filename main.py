import unittest

#기본적으로 아래와 같이 Import를 추천
from chapter2.ch06.pal import Solution

'''
#아래와 같이 Cut & Paste를 해도 된다. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

'''


#메인 함수는 이렇게
if __name__ == "__main__":
    print('hi')

    a = Solution()
    result = a.isPalindrome("ala")

    print(result)



