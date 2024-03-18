#recursion
"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")
show(5)"""#5,4=n-1,3=n-2,2=n-3,1=n-4    

#factorial thru recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    

#sum of first n natural  no
def sum(n):
        if(n==0):
            return 0
        return sum(n-1)+n
print(sum(4))

#all elements in list
def print_list(list,idx=0):
     if(idx==len(list)):
          return
     print(list[idx])
     print_list(list,idx+1)

     
list=[1,4,9,16,25]  
print_list(list)   