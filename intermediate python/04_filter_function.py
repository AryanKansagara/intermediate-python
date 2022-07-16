def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isOdd,a))#-->it filters the number from the list by giving it the function we want
#list(filter(functionname,listwewanttofilter))
print(b)

c = list(map(add7,b))#-->same thing we did above 
print(c)
# also remember that to print anything we need it to be true if return False is written we get empty list

