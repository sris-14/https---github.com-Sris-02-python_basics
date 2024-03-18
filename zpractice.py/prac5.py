#print no 1-100
"""for el in range(1,101):
    print(el)"""
    
#print no 100-1 
"""for el in range(100,0,-1):
    print(el)"""  

#print multiplication table of n
"""a=int(input("enter no you want table of: "))
for i in range(1,11):
    print(i*a)  """      

#print elements of list 
"""num=[1,4,9,16,25,36,49,64,81,100]
for el in num:
    print(el)"""

#search for a number in tuple
"""num1=[1,4,9,16,25,36,49,16,64,81,100]
i=0
x=16
for el in num1:
    #if(num1[i]==x):
    if(el==x):
        print("FOUND at index",i)
        
    i+=1"""

#sum of first n number using while
n=7
i=1
sum=0
while i<=n:
    sum=sum+i
    #print(sum)
    i+=1
print("total sum",sum)    

#factorial of n numbers (for)
n=5
fact=1
i=1
for i in range(1,n+1):
    fact=fact*i
    i+=1
print("factorial of",n,"numbers",fact)    
