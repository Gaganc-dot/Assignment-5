
def even(no1):
    
    if( no1  %2==0):
        print(no1,"is an even number.")
    else:
        print(no1,"is an odd number.")
        
            
def main():
    print("Enter your Number :")
    no1 = int(input())
    
    even(no1)
    

if __name__ == "__main__":
    main()
