
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

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
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            print(i)
            print("result:{}".format(result))
            print("expand1:{}".format(expand(i, i + 1)))
            print("expand2:{}".format(expand(i, i + 2)))


            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        return result



if __name__ == "__main__":

    '''
    a = [1,2,3,4,10]
    print(max(a))
    '''

    a = ["11134", "22323", "32", "sdf4", "10"]
    b = ["1sdfsdf34", "sdgs323", "3werewr2", "swerwerwdf4", "werwer10"]


    print(max(a, b, key=len))



    '''
    a = Solution()
    b = a.longestPalindrome(["1221", "11111111", "tomato", "apppppa"])
    print("final result:{}".format(b))
    '''

