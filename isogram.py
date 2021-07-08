str1="machine"
arr=[]
for i in range(len(str1)):
    arr.append(str1[i])
if(len(arr)==len(set(arr))):
    print("isogram")
else:
    print("not isogram")
