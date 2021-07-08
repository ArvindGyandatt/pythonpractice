mylist=[9,8,6,5,3,8]
arr=[]
m=int(sum(mylist)/len(mylist))

for i in mylist:
    arr.append(abs(m-i))
i=arr.index(min(arr))

print("closest number to mean: ",mylist[i])
