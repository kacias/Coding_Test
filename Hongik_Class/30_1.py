'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            print("===========================")
            print("index:{}".format(index))
            print("char:{}".format(char))

            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:

                print("seen character!")
                start = used[char] + 1
                print("start:{}".format(start))

            else:  # 최대 부분 문자열 길이 갱신

                #if used[char]:
                #    print("start:{} = used[char]:{}".format(start, used[char]))

                print("New character or Reappearance!")
                max_length = max(max_length, index - start + 1)
                print("max_length:{}".format(max_length))

            # 현재 문자의 위치 삽입
            used[char] = index
            print("used:{}".format(used))

        return max_length







if __name__=="__main__":

    #s = "abcabcbb"
    #s = "aaabbbabacb"
    #i = "012345678910"  #인덱스 체크용

    s = "aabbaac"

    a = Solution()
    print(a.lengthOfLongestSubstring(s))

