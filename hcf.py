num1=int(input("enter first number...\n"))
num2=int(input("enter second number...\n"))

if num2>num1:
    mn=num1 # to find shortest no. between two...and then run loop from 1 to shortest number..
else:
    mn=num2

for i in range(1, mn+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print(f"HCF of these two numbers is {hcf}")
