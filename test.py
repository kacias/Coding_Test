
'''
a = input()
list1 = []

#list1 = ["S", "T", "A"]

for i in a:
    list1.append(i)

print(list1)
list1.reverse()
print(list1)



a = "I am boy."
print(a[::-1])

'''

import re
p = re.compile('[a-z]+')
#m = p.match("a")

result = p.findall("life is good")
print(result)