
def rectanglearea(no1,no2):
    ans = no2 * no1
    print("Area is :",ans)

def rectangleperimeter(no1,no2):
    ans = 2 * (no2 + no1)
    print("Perimeter is :",ans)
    
            
def main():
    print("Enter the length :")
    no1 = int(input())
    
    print("Enter the width :")
    no2 = int(input())
    
    rectanglearea(no1,no2)
    rectangleperimeter(no1,no2)
    

if __name__ == "__main__":
    main()