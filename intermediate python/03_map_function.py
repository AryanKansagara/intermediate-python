li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x 
# newList = []
# for x in li:
#     newList.append(func(x))
# print(newList)
#THE ABOVE FOUR LINES CAN BE DONE VERY EFFICIENTLY BY MAP FUNCTION

print(list(map(func,li)))
# print(list(map(li,func))) --->this would give error as the order matters

print([func(x) for x in li if x%2 == 0])#-->here you can give any command and use for loop along with if but mind well those square brackets are important

