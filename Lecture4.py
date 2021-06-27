l=[1,2,4,5,6,7,8,9]
summ = 0
for each in l:
    summ += each 
    print(summ) 
def sum(l):
    if len(l)==0:
        return 0 
    ret=l[0]
    l.remove(l[0])
    return ret + sum(l)
print(sum(l))

