while(True):

    number = int(input("enter no. pz...."))
    
    #if (number==0,1) :
    if number>1:
        for i in range(2 , int(number/2)+1):  #(number/2)+1 in this +1, is specially used for 4 as we know 4/2 is 2 so range become(2 , 2) for loop not run
            if (number%i==0):
                print(number ," is not prime number........")
                break
                
        else:
                print(number," is prime")
                
    else:
        print(number, "is not prime.....")    
    