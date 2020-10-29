'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count
'''

import collections
#===============================================
#디버깅
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in S:
            print("============================")
            if char not in freqs:
                print("char:{}".format(char))
                freqs[char] = 1
            else:
                freqs[char] += 1

            print("freqs:{}".format(freqs))

        # 보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                print("char:{}".format(char))
                count += freqs[char]

        return count


if __name__=="__main__":
    s1 = "bB"
    s2 = "aABbaAb"

    #----------------------------------
    #문제 해석
    #카운터로 딕셔너리 생성 후, s1의 글자의 key값의 value의 합
    print(collections.Counter(s2))
    #---------------------------------


    a = Solution()
    result = a.numJewelsInStones(s1, s2)
    print(result)


