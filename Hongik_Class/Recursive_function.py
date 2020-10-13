#재귀 함수 기초
#https://wayhome25.github.io/cs/2017/04/15/cs-16-1-recursion/
#https://www.fun-coding.org/DS&AL2-3.html


#===============================
'''
#재귀 함수 기본 구조
def Hello(count):

    #1: 종료 조건
    if count == 0:
        return

    #2: 해야 할 일
    print("hello world", count)

    #3: 종료 조건의 변화
    count -= 1

    #4: 재귀 호출
    Hello(count)


Hello(5)
'''

'''
#==================================
#팩토리얼

def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)

print(factorial(5))
'''

#=====================================
#재귀 함수는 for문으로 변환 가능
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(4))

#====================================
#합
'''
def sum(n): # 이 함수의 목표는 0~n 까지의 합을 구하는 것이다
    if n == 0: # n=0 이면 합은 0이다
        return 0
    return n + sum(n-1) # n이 0보다 크면 0에서 n 까지의 합은, n-1까지의 합에 n을 더한 것이다.

print(sum(4)) # 10

'''

#=================================================
#제곱근 구하기
''''
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2,10)) # 1024
'''




#=====================================
#순차 탐색
'''
def search(li, begin, end, target):
    if begin>end:
        return -1
    elif target == li[begin]:
        return begin
    else:
        return search(li, begin+1, end, target)


li = [1,6,10,7,2,5]
target = 10
print(search(li, 0, 5, 10)) # 2
'''

#=============================================
#이진변환
'''
def print_binary(n):
    if n<2:
        print(n, end='')
    else:
        print_binary(n//2)
        print(n%2,end='')

print(10//3)  #몫 정수만 남김 
print(10%2)   #나머지
print(print_binary(1)) #1111
'''

#================================================
#배열의 함
#li[0]에서 li[n-1] 까지의 합을 구하여 리턴
'''
def sum(n, li):
    if n<=0 or n >= len(li):
        return 0
    return li[n-1] + sum(n-1, li)


li = [1,6,10,7,2,5]
print(sum(4, li))
'''


#=====================================================
#피보나치 수열
# 피보나치 수열의 index n의 값을 리턴
# 피보나치 수열 : 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
'''
def fibo(n):
    # 재귀함수는 탈출조건이 꼭 필요하다.
    if n == 0 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

print(fibo(5))
'''

#====================================================
#유클리드 호제법
#참고: 두수의 곱을 최대공약수로 나누면 최소공배수가된다.
'''
def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

print(gcd(48, 60)) # 12
'''

#=====================================================
#하노이 타워
#A에 있는 n개의 원반 중 맨 아래에 있는 n번째 원반을 제외한 나머지 원반을 모두 B로 옮긴다.
#A에 남은 하나의 원반을 C로 옮긴다.
#B의 모든 원반을 C로 옮긴다.
'''
def hanoi(num, _from, _by, _to):
    #탈출 조건
    if num == 1:
        print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
    hanoi(num-1, _by, _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 개수를 입력하세요!(종료 : 0) :"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')
'''
