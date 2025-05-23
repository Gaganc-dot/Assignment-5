def Sum ( no1 , no2):
    ans = no1 + no2
    return ans

def Difference (no1 , no2):
    ans = no1 - no2
    return ans

def Product (no1, no2):
    ans = no1 * no2
    return ans

def Division (no1, no2):
    ans = no1 / no2
    return ans


def main():
    print("Enter your First Number :")
    value1 = int(input())
    print("Enter your First Number :")
    value2 = int(input())
    
    result = Sum(value1, value2)
    print("Sum :",result)
    
    result = Difference(value1, value2)
    print("Difference :",result)
    
    result = Product(value1, value2)
    print("Product :",result)
    
    result = Division(value1, value2)
    print("Division :",result)
    

if __name__ == "__main__":
    main()
