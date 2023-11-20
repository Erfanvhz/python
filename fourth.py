a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [10,11,12]
e = [13,14,15]
f = [16,17,18]
g = [19,20,21]
h = [22,23,24]
i = [25,26,27]
j = [28,29,30]


print(a[0])
print(b[1])
print(c[-1])
print(d[-2])

# extend
j.extend([31,32,33])
print(j)

# append
j.append(34)
print(j)

# insert
j.insert(-1,35)
print(j)

# pop
print(j.pop())