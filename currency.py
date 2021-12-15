with open('allcurrency.txt') as f:
    lines=f.readlines()
    
currencyDict={}
for line in lines:
    parsed=line.split("\t")    
    currencyDict[parsed[0]]=parsed[1]

amout=int(input("Enter amout:\n"))
print("Enter the name of currency you want to convert this amout to? Available options:\n")
[print(item) for item in currencyDict.keys()]# for show currency options...
currency=input("plz enter one of these values:  \n")
print(f"{amout} INR is equal to {amout * float(currencyDict[currency])} {currency}") 
    