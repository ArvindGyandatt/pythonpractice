str1='arvind'
arr=[]
for i, val in enumerate(str1[:]):
    u=str1[i].upper()
    a=str1.replace(str1[i],u)
    arr.append(a)
print(arr)
