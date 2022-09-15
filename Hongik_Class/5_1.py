import collections
from typing import List

'''
그룹 애너그램 
Input : ["eat", "tea", "tan", "ate", "nat", "bat"]
Output : 
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

설명 : "ate", "eat", "tea"는 모두 글자의 배치만 바뀌었을 뿐 구성 글자는 모두 같기 때문에 anagram들이라고 할 수 있습니다. 그렇기 때문에 이들을 그룹 지어서 리턴합니다. 마찬가지로 "nat", "tan"도 그렇고, "bat"는 그룹이 없기 때문에 혼자 그룹을 이룹니다.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        print("anagrams:{}".format(anagrams))
        return list(anagrams.values())


def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter


if __name__ == "__main__":

    #---------------------
    #딕셔너리 사용법

    '''
    test = {'a':1, 'b':2}

    print(test)
    print(test['a'])


    for keys, value in test.items():
        print(keys)
        print(value)
    '''

    #---------------------
    #defaultDic
    '''
    #목차로 사용할 리스트가 있고
    s = ['a', 'b', 'c', 'd', 'a']

    #디폴트로 사용할 값을 정의해서
    d = collections.defaultdict(int)

    for k in s:
        d[k] += 1
        print(d)

    #이렇게 해야 딕셔너리로 변환
    print(dict(d))

    '''


    #=========================
    #.join()
    '''
    a = ["1","2","3","4"]

    #리스트 각 요소 사이에 특정 문자열을 집어넣을 때
    b = ":".join(a)
    print(b)

    #리스트 모든 값을 합칠 때
    b = "".join(a)
    print(b)
    '''

    '''
    aa = countLetters("I am boy")
    print(aa)
    '''



    a = Solution()
    b = a.groupAnagrams(["apple", "banana", "tomato", "ppale"])
    print(b)
