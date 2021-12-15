while(True):
    number = int(input("enter no. pz.."))
    if number > 2:
          
        for i in range(2, int(number/2)+2):  # (number/2)+1 in this +2, is specially used for 3 as we know 4/2 is 2 so range become(2 , 2) for loop not run
            if (i * i == number):
                    print(i, "is square root of...." , number)
                    break
                    
                    

        else:
                    print(number, " HAVE NOt COMPLETE SQUARE ROOT")
                    
                    


    else:
        print("Enter no. greater than Two")
#maintain squence of loops , in this way for loop check range and condition in one time........