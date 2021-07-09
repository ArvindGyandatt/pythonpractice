 t='5:70:65'
 a=t.split(":")
 hrs=int(a[0])
 min=int(a[1])
 sec=int(a[2])
 
 if(sec>59):
     min+=1
     sec=sec-60

 if(min>59):
     hrs+=1
     min=min-60

 t=str(hrs)+":"+str(min)+":"+str(sec)
 print(t)
