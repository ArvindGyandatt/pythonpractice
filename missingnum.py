list1=[5,2,1,3,8,9]
list2=[5,2,1,8,9]
d=set(list1)-set(list2)
print("missing num : ",*list(d))
