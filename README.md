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
