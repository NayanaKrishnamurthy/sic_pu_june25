## given server1 and server2 allocation +ve value ,deallocation -ve value.
## given values be[2gb,-4b,6gb,-3gb]-->[server1,server2,server1....]
# given to print total number of unit memory of server 1 that is evenplaces in the list.

list1=[24,3,34,-2,-3,-6,3,-6]
sum=0
for i in range(len(list1)):
    if int(i)%2==0:

        sum+=(list1[i])
print(sum)