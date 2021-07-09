# python codes

1. In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)

mylist = [2,2,2,2,3]

n= len(mylist)

res = mylist[0]

for i in range(1, n):
    res = res ^ mylist[i]

print(res)


2. In a given list of elements, find the elements which is close to its mean

