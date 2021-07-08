hrs=2
min=86
sec=93
if(sec>59):
    min+=1
    sec=sec-60

if(min>59):
    hrs+=1
    min=min-60

t=str(hrs)+":"+str(min)+":"+str(sec)
print(t)
