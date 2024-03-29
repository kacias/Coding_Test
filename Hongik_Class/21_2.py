import collections

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
'''

#디버깅
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        print("input_s:{}".format(s))
        print("seen:{}".format(seen))


        for char in s:
            print("==================")

            print("char:{}".format(char))
            print("counter[char]:{}".format(counter[char]))
            print("seen_before:{}".format(seen))
            print("stack_before:{}".format(stack))

            counter[char] -= 1

            if char in seen:
                print("continue--->")
                continue

            # 뒤에 같은 숫자가 있다면 스택에서 없애고, Seen에서도 없앤다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print("++++++++")
                print("seen:{}".format(seen))
                print("stack:{}".format(stack))

                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

            print("seen_after:{}".format(seen))
            print("stack_after:{}".format(stack))


        return ''.join(stack)



    
if __name__=="__main__":
    '''
    d = "aabbcd"
    print(collections.Counter(d))
    e= [1,2,4,2,3,1]
    print(collections.Counter(e))
    f = "kangkangkang"
    print(collections.Counter(f))

    g = {5,6,3,3,3}
    print(collections.Counter(g))
    '''

    #f= {"a":1, "a":1, "c":5}
    #print(collections.Counter(f))

    '''
    g = [1,2,5,10]
    print(g[-1])
    print(g)
    
    #문자들간의 크기 비교는 아스키값 기준
    l = ["a", "b", "c", "c"]
    for c in l:
        if c < l[-1]:
            print("confirm:{}".format(c))

    '''
    '''
    #set 데이터
    dd = {1,3,5,6,9,9}
    print(dd)
    dd.add(10)
    print(dd)
    #----------------------
    '''

    s = "cbaeabc"
    #s = "ebcabc"
    a = Solution()
    result = a.removeDuplicateLetters(s)
    print(result)
