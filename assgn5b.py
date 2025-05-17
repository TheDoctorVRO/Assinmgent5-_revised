lis = []
for _ in range(10):
   lis.append(_)

print('original list ', lis)

a= lis[0:5]
print('extracted 5 elements',a)

a.reverse()
print('reverse list ',a)

b=a[::-1]
print('reversing above list again ',b)   
