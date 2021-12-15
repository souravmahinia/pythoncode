while(True):
    n = int(input("Enter value of n-----"))
    k=2*n-2    # K variabe take for spaces.. for exampe if n=5 spaces =8
    if n > 0:
          
        for i in range(0, n): #this outer loop is for represting number of row

            for j in range(0, k):# this is for spaces
                print(end=" ")# end is for  change column
                
            k=k-2
            for j in range(0, i+1): # for column
                print("*" ,end=" ")

            print("\r")     


    else:
        print("enter no. greter than ZERO")

