
def fahrenheit(no1):
    ans = (no1 * 9/5) + 32
    print("Temperature in Fahrenheit :",ans,"F")
            
def main():
    print("Enter the Temperature in celsius :")
    no1 = int(input())
    
    fahrenheit(no1)
    

if __name__ == "__main__":
    main()