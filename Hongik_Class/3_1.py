from typing import List


'''
주어지는 input에는 두 가지 특성의 데이터가 존재한다. 하나는 'letter-logs'이고 다른 하나는 'digit-log'이다. 그리고 output은 다음과 같은 제약조건을 가진다.
logs의 각 인자의 첫번째 단어를 identifier로 칭한다.
letter-log는 digit-log보다 먼저 정렬되어야 한다.
letter-log는 identifier을 무시하고 다음 단어부터 사전식 정렬순을 가진다. 만약 사전식 정렬이 같을 경우 identifier를 고려한다.
digit-log는 input과 같은 순을 가진다.
그렇기 때문에 input에서 letter-log와 digit-log를 구분해야 했으며, 첫번째 단어의 글자의 형식(숫자인지 문자인지, isnumeric())에 따라 둘을 구분하였다. 그리고 letter-log의 순서는 먼저 첫번째 단어(identifier) 이후의 단어로 정렬하고 그 다음 첫번째 단어(identifier)로 정렬해서 digit-log와 합친 후(순서대로 append 되었다) 결과를 구한다.
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            print("-----------")
            print(log)

            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

            print("letter:{}".format(letters))
            print("digit:{}".format(digits))

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


if __name__ == "__main__":


    #-----------------------
    #split()
    '''
    a = "naver daum"
    b = a.split()
    print(b)
    '''

    '''
    a = "naver*daum"
    b = a.split("*")
    print(b)   
    '''

    '''
    a = "naver daum"
    b = a.split()[0]
    c = a.split()[1]
    print(b)
    print(c)
    '''

    #--------------------------
    #isdigit()
    '''
    e="111"
    f="abc"
    print(e.isdigit())
    print(f.isalpha())
    '''


    a = Solution()
    b = a.reorderLogFiles(["dif1 8 1 5 1", "a345 8 1 5 1", "a345 bert b c", "lef2 bert b c"])
    print(b)



    #----------------------
    #람다식
    '''
    a = lambda x: x*x
    print(a(2))

    b = lambda x: (x+x)^2
    print(b(2))
    '''

    '''
    #튜플로 반환
    bouble_return = lambda x: (x+1, x-1)
    print(bouble_return(2))
    print(type(bouble_return(2)))
    '''

    '''
    #리스트로 반환
    b = lambda x: [x+1, x-1]
    print(b(2))
    print(type(b(2)))
    '''

    '''
    #람다 함수와 리스트의 결합 map
    a = [1,2,3]
    c = list(map(lambda x: x+1, a))
    print(c)
    print(type(c))
    '''

    '''
    #람다 함수와 2개의 리스트의 결합 map
    a = [1,2,3]
    b = [5,6,7]
    c = list(map(lambda x, y: x+y, a, b))
    print(c)
    print(type(c))
    '''

    #-----------------------
    #sort
    '''
    a= [1,5,4,3]
    a.sort()
    b = sorted(a)
    print(a)
    print(b)
    '''

    '''
    c = {"c":1, "b":2, "a":3}
    e = {2:"hi", 1:"ne", 3:"ke"}

    #sort는 리스트만
    #c.sort()
    #print(c)


    #sorted 는 딕셔너리도 가능
    #key 값 기준으로 정렬됨
    d = sorted(c)
    print(d)

    k = sorted(e)
    print(k)
    print(k[2])
    '''


    student_tuples = [
    ('john', 'A', 15),
    ('jane', 'C', 10),
    ('dave', 'B', 10),
    ]


    '''
    #정렬 기준값
    f = sorted(student_tuples, key = lambda x: x[2])
    print(f)
    '''

    '''
    g = sorted(student_tuples, key=lambda x: x[1])
    print(g)

    '''

    '''
    k = sorted(student_tuples, key= lambda x: (x[2], x[1]))
    print(k)
    '''


    '''
    k = sorted(student_tuples, key= lambda x: (x[1], x[2]))
    print(k)
    '''
