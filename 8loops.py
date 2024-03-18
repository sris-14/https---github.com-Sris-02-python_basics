#while loop
"""count=1
while count<=5:
    print(count,"Hello!")
    count+=1"""

#break
"""tup=(1,4,9,16,34)
x=16
i=0
while i<len(tup):
    if(tup[i]==x):
        print("FOUND")
        break
    else:
        print("finding...")
    i+=1  """      

#continue
"""i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1    """

#for loop
"""list=[1,2,3]
for el in list:
    print(el)"""

#for loop with else
#1.
"""for el in list:
    print(el)
else:
    print("END")   """ 
#2.
"""str="apnacollege"

for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("END") """   

#range
#1.
"""for el in range(1,50):
    if(el%2==0):
        print(el)
#2.        
for el in range(1,5,2):#range(start?,stop,step?)
    print(el)"""        

#pass statement
for i in range(5):
    pass

print("pass statament (null statement) that does nothin'.\nIt's a placeholder.")    

if i>5:
    pass