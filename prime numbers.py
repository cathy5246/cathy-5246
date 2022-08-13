
        
def value ():
    var =input("Enter a whole number: ")
    return var
print(value())


def primeChecker(a):
    if a > 1:
        for j in range(2,int(a/2)+1):
            if (a % j) == 0:
                print (a, "is not a prime number.")
                break
            else:
                print(a, "is a prime number.")
                break
        else:
            print(a, "is not a prime number.")
            
a = int(input("Enter an whole number: "))
primeChecker(a)

start = int(input("Enter the starting range: "))
end = int(input("Enter the end range: "))
print("Prime numbers in the range are", start, "to", end)
for i in range(start, end+1):
    flag = 0
    for L in range (2,i):
        if (i % L ==0):
            flag = 1
            break
    if (flag == 0):
        print (i, end = ' ')
        
