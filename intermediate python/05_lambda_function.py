# def func(x):
#     return x+5
# print(func(2))
# ----------------
#instead you can use this too as a fucntion no need to write two line code 
# func2 = lambda x: x+5
# print(func2(9))
# ------------------
#example of lambda inside a function 
# def func(x):
#     func2 = lambda x: x+5
#     return func2(x) + 40
# print(func(2))
# --------------------
#for multiple parameters
# func = lambda x,y :x + y
# print(func(43,43))
# ---------------------
# a = [1,2,3,4,5,6,7,8,9,10]
# newList = list(map(lambda x:x+5,a))
# newList2 = list(filter(lambda x:x%2==0,a))
# print(newList)
# print(newList2)
# ---------------------