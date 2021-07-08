numbers=35813
num=str(numbers)
res=[]

for i in range(len(num)):
    res.append(int(num[:i]+num[i+1:]))
print(max(res))
