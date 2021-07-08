mylist = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]

sum = 0
n= len(mylist)

for i in range (0,n):
    sum += mylist[i]

print("for time =1 avg. speed is: ", sum/n)
