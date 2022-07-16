import collections
from collections import Counter

#containers
#list
#set
#dict
#tuple - inmuttable

c = Counter('gallad')
print(c)
c = Counter(['a','b','c'])
print(c)
c = Counter({'a':1,"b":2})
print(c)
c = Counter(cats=4,dogs=5)
print(c['cats'])#--->specifically calling the cats value
#if it were a dictionary and say print(c['pet']) would have been written then it would give error whereaas counter doesnot
print(list(c.elements()))

print(c.most_common(1))#this gives the mostcommon element and its count as well
f = Counter(a=3,b=4,d=3 )
d = ['a','b','d']
f.subtract(d)#this subtracts we just need to call it 
print(f)
f.update(d)
print(f)#this will update it from the last counter method we performed

f.clear()#empties out f
print(f)

'''
we can do 
c+d
c-d
when the counter is less than equal to 0 while doing above 
for intersection we do
c & d
for union 
c | d
'''