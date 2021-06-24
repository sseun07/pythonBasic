'''
Where do you use for-loop? 
RANGE-함수
- range(a,b) *a is optional (is inclusive) // a 보다 크거나 같고, b 보다는 작은것 
- create list
'''
for each in range(16,25): 
    print(each)

l=[1,2,3,7,10,20,35]
print(l[0])
for each in range(len(l)):
    print(l[each])

'''
len=length of the list
'''
'''
NEGATIVE INDEX 
l[-1] : 뒤에서 첫번째 l[-2] : 뒤에서 두번째
print(l[-1]) 
'''
#HW: for loop 은 어디에 쓰는지 RESEARCH by (2021.06.24 7pm)
#used to iterate over a sequence (either list, tuple, dictionary, set, or string).
#for loop allows to sort list like/such as [0,5,4,2] >> [0,2,4,5]
#2D List: l=[[1,2,3],[4,5,6]] **list 안에 list 
#3D List: l=[[1,2,3],[4,5,6,[7,8]]]
#4D List: l=[[1,2,3],[[[4,5]]]] >> 이렇게 멀리까지 가면 속도가 느려짐 
#for loop 을 Range 1=한번 돌린다 면 괜찮음
'''
l=[[1,2,3],[4,5,6]]
for each in l:
    for number in each: 
        print(number) = 1,2,3,4,5,6

l=[[1,2,3],[4,5,6]]
print(l[0][0]) = 1 (index)
'''
l=[[1,2,3],[4,5,6]] #2x3
print(l[0])
for each in range(len(l)): 
    for number in range(len(l[each])):
        print(l[each][number])
    #But what if the list was: [1,2,3], [4,5,6,7] >> there are list like this but bit difficult to use as above for loop
 #HW: Frequency that our eye perceives // Need to create and   explain about "sorting algorithm using for loop"
