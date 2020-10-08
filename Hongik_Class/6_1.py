
#가장 긴 팰린드롬 부분 문자열

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        
        return result
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                print("left:{}".format(left))
                print("right:{}".format(right))
                left -= 1
                right += 1

            #발견된 서브 스트링 반환
            return s[left + 1:right - 1]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            print("----------------------")
            print("iter:{}".format(i))
            print("character:{}".format(s[i]))
            print("result:{}".format(result))
            print("expand1:{}".format(expand(i, i + 1)))
            print("expand2:{}".format(expand(i, i + 2)))

            #현재까지 발견된 가장 서브 스트링 팰린드롬
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        return result



if __name__ == "__main__":

    a = Solution()
    b = a.longestPalindrome("aabbccc")
    print("final result:{}".format(b))


    #==========
    #중첩 함수

    '''
    #==============
    #숫자일 경우 가장 큰 값

    a = [1,2,3,4,10]
    print(max(a))

    #===========================
    #문자열 리스트일 경우 맨 "앞글자"를 기준으로 알파벳 순 정렬로 가장 뒤에 있는 거
    c = ["Python", "Z Programming", "Java", "JavaScript", "Za"]
    d = max(c)
    print(d)


    #------------------
    #키 값을 Len 지정하면 가장 긴 문자열 반환
    f = max(c, key=len)
    print(f)


    #------------------------------
    #여러개 숫자 경우 가장 큰 값
    #result = max(4, -5, 23, 5)
    result = max("aaa", "bbbb", "ddddddd", key=len)
    print("The maximum number is:", result)


    #-------------------------------
    #람다함수 사용
    names = ['Suh', 'Adrian', 'Bill', 'Jonathan']
    longest = max(names, key= lambda n: len(n))
    print(longest)

    #------
    #slicing
    s = [0,1,2,3,4]
    print(s[3])
'''
