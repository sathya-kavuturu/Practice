import array as arr

a = arr.array('d',[1,2,3,4,5,6,7])
print(a)

#adding elements
a.append(8)
print(a)

#extending
a.extend([9,10,11,12])
print(a)

#pop
a.pop()
print(a)