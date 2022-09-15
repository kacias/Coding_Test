import unittest

#from chapter2.ch06.pal import Solution

class Solution:
    def isPalindrome(self, s):
        strs = []

        for char in s:
            #print("char:{}".format(char))
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

if __name__ == "__main__":
    #a = [1, 2, 4]
    #print(a.pop())


    a = Solution()
    result = a.isPalindrome("112411")
    print(result)

