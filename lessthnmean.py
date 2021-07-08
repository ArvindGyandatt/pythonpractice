mylist=[9,8,6,5,3,8]

r =sum(mylist)/len(mylist)

#print(r)

for i in range (0,len(mylist)):

    if (mylist[i]<r):
        print(mylist[i])
