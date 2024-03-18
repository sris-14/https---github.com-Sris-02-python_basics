# # file i/o
# f=open("demo.txt","a")

# #READ:
# # data=f.read(5)
# # print(data)
# # print(type(data))
# """line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)"""

# # WRITE:
# f.write("\nNow append is used")

# f=open("sample.text","a")

# # prac 2,3,4 for more
# f.close()

"""f=open("demo.txt","a+")
# f.write("abc")
print(f.read())
f.write("\nabc")
f.close()"""

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

import os
os.remove("demo.txt")
