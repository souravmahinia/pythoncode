while(True):
    number = int(input("Enter no. to find Factorial....."))
    if number > 1:
          
        for i in range(1, number):
            fac=(number*i)
            number=fac
            
        print("Factorial is ", number)  # if print is not equal to for loop then number is printing always............
                    
    else:
        print("1")