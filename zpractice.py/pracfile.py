"""with open("practice.txt","r") as f:
    data=f.read()"""

#replace java with python
"""new_data=data.replace("Java","python")    
print(new_data)
with open("practice.txt","w") as f :
    f.write(new_data)"""

#finding a word in file
"""def check_word():
    word="learning"  
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("FOUND")
        else:
            print("not found") 
check_word()   """  

#find in which line does the word "learning" occure first.
"""def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1    
    return -1

print(check_for_line()) """               

#containing no separated by comma, print the count of even no
# 1,2,45,55,76
count=0
with open("prac.txt","r")as f:
   data=f.read()
   print(data)
#individual no
   #scratch wala method    
   """num=""
   for i in range(len(data)):
      if(data[i]==","):
         print(int(num))
         num=""
      else :
         num+=data[i]  """ 
   num=data.split(",")
   for val in num:
      if(int(val)%2==0):
         count+=1
   print(count)

#parse/convert/typecasting to int    
