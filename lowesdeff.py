mylist = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]

x=min(mylist)
mylist.remove(min(mylist))
y=min(mylist)
print("lowest diff. is",y-x)
