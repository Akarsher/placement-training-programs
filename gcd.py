# gcd of 2 numbers
def gcd(a, b):     
    while b: 
        a, b = b, a % b
    return a  
  
num1 = int(input("Enter Num 1 : "))  
num2 = int(input("Enter Num 2 :"))  
  
result = gcd(num1, num2)  
print("GCD : ",result) 
