
def Largest(no1,no2,no3):
    
    if( no1 >= no2):
        if(no1 >= no3):
            return no1
        else :
            return no3
    else:
        if(no2 >= no3):
            return no2
        else:
            return no3
            
def main():
    print("Enter your 1st Number :")
    no1 = int(input())
    
    print("Enter your 2nd Number :")
    no2 = int(input())
    
    print("Enter your 3rd Number :")
    no3 = int(input())
    
    result =Largest(no1,no2,no3)
    print("Largest Number is :",result)
    

if __name__ == "__main__":
    main()
