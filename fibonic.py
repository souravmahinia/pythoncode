# In fibonacci series next number is the sum of previous two number.....
while(True):
    a=0
    b=1
    num = int(input("Enter no. of elements....  "))
    if (num==0):
        print(a)
    elif(num==1):
        print(b)
    else:
        for i in range(1,num): #(1,num) is define range according to input(ONE LESS THAN INPUT)
            c = a+b #after this c=1
            a = b# after this a=1
            b = c # after this b = 1
            print(b) # print = 1 but after this now a = 1 so next time c = 2 so print = 2 ........continue

