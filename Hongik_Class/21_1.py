class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

#======================================================
#디버깅 코드
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            print("====================")
            print("input_s:{}".format(s))
            print("char:{}".format(char))
            suffix = s[s.index(char):]
            print("suffix:{}".format(suffix))
            # 전체 집합과 접미사 집합이 일치할때 분리 진행
            if set(s) == set(suffix):
                print("set:{} == set_suffix:{}".format(set(s), set(suffix)))
                print("go deeper! char is removed")
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''



if __name__=="__main__":

    #=====================
    #set 집합 문법 연습
    #딕셔너리  {"a": 1, "b": 2}
    #셋 {'a', 'b'}


    set1 = {5,7,10}
    print(set1)
    set1.add(100)
    set1.remove(5)
    set1.discard(77)
    print(set1)

    set2 = set([1,4,5])
    print(set2)

    #문자열을 set로 사용해서 sorted 시키면 기본 구성 요소끼리 정렬시킬 수 있음 
    s = "abcdefff"
    print(set(s))
    print(sorted(set(s)))

    #==========================
    #문자열 내에서 특정 char 인덱스 값
    print(s.index("c")) #해당 character가 있는 index 값 반환
    print(s[s.index("c"):]) #해당 character 있는 index 이후 문자열 반환


    #-----------------------
    s= "abcabcee"
    a = Solution()
    result = a.removeDuplicateLetters(s)
    print(result)
