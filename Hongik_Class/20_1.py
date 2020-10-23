'''
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
'''

#디버깅
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        print("input:{}".format(s))

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            print("==========================")
            print("char:{}".format(char))
            print("table_before:{}".format(table))
            print("stack_before:{}".format(stack))

            if char not in table:
                print("pass1")
                stack.append(char)
                print("stack added:{}".format(stack))

            elif not stack or table[char] != stack.pop():
                print("pass2")
                return False

            print("stack_after:{}".format(stack))


        return len(stack) == 0




#======================================
#메인 함수

if __name__=="__main__":

    #-----------------------
    s= "()[]{}"
    a = Solution()
    result = a.isValid(s)
    print(result)

