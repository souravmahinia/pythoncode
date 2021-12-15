while(True):

    number1 = int(input("enter Ist no. pz.."))
    number2 = int(input("enter 2nd no. pz.."))
    print("Before Swap...",number1,number2)
    number1=number1*number2
    number2=number1/number2
    number1=number1/number2
    print("After swaped....",number1,number2)