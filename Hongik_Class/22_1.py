from typing import List

'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
'''

#디버깅
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        print("input T:{}".format(T))
        print("answer:{}".format(answer))
        print("stack:{}".format(stack))
        print("begin --------------------------------------->")

        for i, cur in enumerate(T):
            print("============================")
            print("i:{}".format(i))
            print("cur:{}".format(cur))
            print("stack_before:{}".format(stack))

            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                print("++++++++++++")

                last = stack.pop()
                print("last:{}".format(last))
                answer[last] = i - last
                print("answer[last]:{}".format(answer[last]))
                print("answer:{}".format(answer))
                print("stack_inside:{}".format(stack))

            stack.append(i)
            print("stack_after:{}".format(stack))

        return answer



if __name__=="__main__":

    #-----------------------
    s= [73, 74, 75, 71, 69, 72, 76, 73]
    a = Solution()
    result = a.dailyTemperatures(s)
    print("result:{}".format(result))


