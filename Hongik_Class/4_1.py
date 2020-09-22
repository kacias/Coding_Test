import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]

if __name__ == "__main__":


    '''
    a = Solution()
    b = a.mostCommonWord("apple banana", ["apple", "red"])
    print(b)
    '''

    #==============================================
    #리스트를 한줄로 만드는 기법
    #list comprehension


    #기존 방식
    number = []
    for i in range(0, 6):
        number.append(i)
    print(number)

    #리스트 컴프리핸션
    number2 = [i for i in range(0, 6)]
    print(number2)

    #리스트 컴프리핸션 조건문
    number3 = [i for i in range(0,6) if i%2 == 0]
    print(number3)

    #리스트 컴프리핸션 항목 제외
    baned = [3,5]
    number3 = [i for i in range(0,6) if i not in baned]
    print(number3)

    # 리스트 컴프리핸션 항목 중복
    union = [3,5]
    number3 = [i for i in range(0,6) if i in baned]
    print(number3)

    #무난하게 푸는 법
    name = ["Kang", "Kim", "Cho", "Kang", "Kim"]
    result = collections.Counter(name)
    print(result)
    print("result most common:{}".format(result.most_common()))
    print("result most common:{}".format(result.most_common()[0]))
    print("result most common:{}".format(result.most_common()[0][0]))

    lower_name = []
    for i in name:
        lower_name.append(i.lower())
        print(i)
    print(lower_name)


    #name_list = [i for i in name]
