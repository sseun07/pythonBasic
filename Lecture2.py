#If Statement: If ~ is true do the following (true=2수를 compare= True 이면 실행되는거)
#elif (eliseif): if 문이 만족하지 않았을 때 elif로 넘어와 다시 비교를 한다
#else: 위에 해당이 없을 때 
from typing import List


a=4
b=4
c=True

if b<a:
    print('a is bigger than b') 
elif c!=True:
    print('c is True')
elif a<b:
    print('b is bigger than a')
else:
    print('noneoftheabove')
'''
#list: 숫자/sting/etc 등을 하나에 묶어 버리고 싶을 때 씀
l = []
l = list()
[1,2,41,4,2,3,1,'a'] python 만 다른언어들과 string, complex 등 을 묶을 수 있음.
Index= list의 순서, #1=0번째 자리 
print(l[0])>>0번째 index print 방법
'''
l = [1,'a', 3, 'ab', 4, 5]
print(l)

l.append('nbgy') 
print(l)

l.remove(1)
print(l)

print(l[1])
l.insert(3, 'alpha')
print(l)
l.pop(3)
print(l)
'''
# 길이가 5인 list가 있을 때 그 list 는 자연수로만 이루어져있다. 그럴때 그 자연수들의 합을 구하라. 힌트=index
#l=[1,2,3,4,5]
#summ = 0
#for each in l:
    #for loop (위에꺼) ///// summ += each >> summ = summ + each
    #summ += each 
    #l.append(9)
    #print(summ)
'''

#HW: for loop 을 사용해서 list 안에 있는 원소들의 합을 구하시오. 
l=[6,7,8,9,10,11,12]
summ = 0
for each in l:
    summ += each 
    print(summ) 
    #=63