# python codes

1. In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)

        mylist = [2,2,2,2,3]

        n= len(mylist)

        res = mylist[0]

        for i in range(1, n):
            res = res ^ mylist[i]

        print(res)


2. In a given list of elements, find the elements which is close to its mean

        mylist=[9,8,6,5,3,8]
        arr=[]
        m=int(sum(mylist)/len(mylist))

        for i in mylist:
            arr.append(abs(m-i))
        i=arr.index(min(arr))

        print("closest number to mean: ",mylist[i])

3. Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]

        
        mylist = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]

        sum = 0
        n= len(mylist)

        for i in range (0,n):
            sum += mylist[i]

        print("for time =1 avg. speed is: ", sum/n)
       
 4. Find the no.of people in a bus, given the data of people onboarding & alighting at each station

        onboard=["rutwik","anurag","pranav","mukesh","anubhav", "harish"]
        alighting=["mukesh","anubhav", "harish"]
        d=len(set(onboard)-set(alighting))
        print(d)
5. Find the missing number, given the original list and modified one
        
        list1=[5,2,1,3,8,9]
        list2=[5,2,1,8,9]
        d=set(list1)-set(list2)
        print("missing num : ",*list(d))
        
6. Find the difference between two lowest numbers in the list

        mylist = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
        x=min(mylist)
        mylist.remove(min(mylist))
        y=min(mylist)
        print("lowest diff. is",y-x)
        
7. In a given list, count no.of elements smaller than their mean

        mylist=[9,8,6,5,3,8]

        r =sum(mylist)/len(mylist)

        #print(r)

        for i in range (0,len(mylist)):

            if (mylist[i]<r):
                print(mylist[i])
 
8. Correct the malformed time string , for e.g "5:70:65" to "6:11:05"
        
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
        
9. Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018"

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
        
10. Convert ip address from "a.b.c.d" format into integer and vice versa
        
        def is_valid(ip):
            ip = ip.split(".")
            for i in ip:
                if (len(i) > 3 or int(i) < 0 or
                        int(i) > 255):
                    return False
                if len(i) > 1 and int(i) == 0:
                    return False
                if (len(i) > 1 and int(i) != 0 and
                        i[0] == '0'):
                    return False

            return True

        def convert(s):
            sz = len(s)

            if sz > 12:
                return []
            snew = s
            l = []

            for i in range(1, sz - 2):
                for j in range(i + 1, sz - 1):
                    for k in range(j + 1, sz):
                        snew = snew[:k] + "." + snew[k:]
                        snew = snew[:j] + "." + snew[j:]
                        snew = snew[:i] + "." + snew[i:]

                        if is_valid(snew):
                            l.append(snew)

                        snew = s

            return l

        A = "25525511135"
        B = "25505011535"

        print(convert(A))
        print(convert(B))
        
11. Check whether given string is isogram or not

        str1="machine"
        arr=[]
        for i in range(len(str1)):
            arr.append(str1[i])
        if(len(arr)==len(set(arr))):
            print("isogram")
        else:
            print("not isogram")
            
12. Given a string, find the mexican wave
 
        str1='arvind'
        arr=[]
        for i, val in enumerate(str1[:]):
            u=str1[i].upper()
            a=str1.replace(str1[i],u)
            arr.append(a)
        print(arr)
        
13. iven a number, find the largest number by deleting single digit (order of digits will remain same)
15. Given a number, find the largest number by shuffling the digits
16. Compute the word frequency in given message
17. RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF
18. Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd
