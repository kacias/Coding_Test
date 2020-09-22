import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

result = p.findall("life is too short")
print(result)

string = "jhgjhgjh2324sdljlkjlafj 786876"
string = string.strip()
print(string)
result2 = re.findall("[0-9]+", string)
print(result2)


if __name__ == "__main__":
    a = [1, 2, 4]
    print(a.pop())

    '''
    a = Solution()
    result = a.isPalindrome("111111")
    print(result)
    '''

