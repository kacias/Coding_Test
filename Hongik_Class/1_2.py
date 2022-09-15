
import collections
from typing import Deque
import re
#Deque 의 사용
#https://www.hanbit.co.kr/network/category/category_view.html?cms_code=CMS3942847236
#https://excelsior-cjh.tistory.com/96

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            #popleft()
            if strs.popleft() != strs.pop():
                return False
        return True
'''


#정규식 사용법
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링

        s = re.sub('[^a-z0-9]', '', s)        
        #print(s[::-1])
        return s == s[::-1]  # 슬라이싱


if __name__ == "__main__":
    '''
    a = [1, 2, 4]
    print(a.pop())
    '''

    
    a = Solution()
    result = a.isPalindrome("A22a")
    print(result)
    

    '''
    s= "aaabbb"
    b = s[1:4]
    print(b)
    '''

    
    #===============
    #deque 사용
    '''
    a = collections.deque([1,2,3])
    print(a)
    a.popleft()
    a.append(4)
    a.append(5)
    a.pop()
    print(a)
    '''
    #===============
    



