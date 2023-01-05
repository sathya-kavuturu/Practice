# #map
# li =['dagdg', 'gageg','1',  'ergergerg', 'ergetgrthrth']
# def upper_case(item):
#     return item.upper()
# 
# print(list(map(upper_case, li)))


# filter


#zip
# li1 = ['sathya', 'lohith', 1, 'santhosh', 'vikas']
# li2 = [1,2,3,4,5]
# li3 = [10,20,30,40,50,60,70]
# 
# print(list(zip(li1,li2,li3)))

#reduce


#lambda functions
#squaring list
# li = [1,2,3,4,5,6,7,8,9]
# print(list(map(lambda item:item*item, li)))


#list sorting
# li = [(0,2), (4,3),(9,9),(10,-1)]
# li.sort(key = lambda x: x[1])
# print(li)


#list comprehensions
# import math
# li = [math.sqrt(num) for num in range(0,101) if num%2 !=0]
# print(li)


#set comprehensions
# se = [num for num in range(0,101) if num%2 !=0]
# print(se)


#dictionary comprehensions
# import math
#di = {'a':2, 'b':5, 'c':6, 'd': 3, 'e': 8}
# dict1 = {key: math.sqrt(value) for key,value in di.items()}
# print(dict1)


# di = {'a':2, 'b':5, 'c':6, 'd': 3, 'e': 8}
# dict1 = {k:v for k,v in di.items() if v%2==0}
# print(dict1)


# dict1 = {num:num*2 for num in [1,2,3,4,5]}
# print(dict1)


#exercise

# li = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'f', 'g']
# duplicates=[]
# duplicates = list(set([x for x in li if li.count(x)>1]))
# print(duplicates)












