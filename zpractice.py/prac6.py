# print length of  a list(list is a paramter)
"""def len_list(list):
    return len(list)
list=[1,4,9,16,36,49,64,81,100]
print(len_list(list))"""

# print elements of a list in a single line
# def print_ele(list):
#     return list
# list=[1,4,9,16,36,49,64,81,100]
# print(list)
"""places=["delhi","chandigarh","noida","gorakpur","pink city","vrindavan"]
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(places)   """     

# factorial
"""def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("enter no for factorial:"))
print(calc_fact(n))"""

#USD ---> INR
"""def conver_currency(usd_val):
    # inr=83.02
    inr_val=usd_val*83.02
    print(usd_val,"USD =",inr_val,"INR")
conver_currency(73)"""

#hw
def odd_even(n):
    # n=int(input("enter no:"))
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
odd_even(int(input("enter number:")))            