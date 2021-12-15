while(True):
    n = int(input("Enter value of n-----"))
    if n > 0:
          
        for i in range(0, n): #this outer loop is for represting number of row

            for j in range(0, i+1):# this inner loop is for column
                print("*" ,end=" ")# end is for  change column

           
            print("\r")# for change row.


    else:
        print("enter no. greter than ZERO")