 d='49/07/2028'
 a= d.split("/")
 days = int(a[0])
 month = int(a[1])
 years = int(a[2])
 

 m31=[1,3,5,7.8,10,12]
 m30=[4,6,9,11]

 days=int(a[0])
 month=int(a[1])
 year=int(a[2])

 if month in m31:
     if(days>31):
         month+=1
         days=days-31

 elif month in m30:
     if(days>30):
         month+=1
         days=days-30

 elif month == 2:
     if(days>28):
         month+=1
         days=days-28


 if(month>12):
     years+=1
     month=month-12

 date=str(days)+"/"+str(month)+"/"+str(year)
 print(date)
