days=45
month=8
year=2018
if(days>31):
    month+=1
    days=days-31

if(month>12):
    years+=1
    month=month-12

date=str(days)+":"+str(month)+":"+str(year)
print(date)
