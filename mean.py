mylist = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]

print(list((a) for a in mylist if a<sum(mylist)/len(mylist)))
