
def vote(no1):
    
    if( no1 >= 18):
        print("Eligible to vote")
    else:
        print ("Not eligible to vote")


def main():
    print("Enter your age :")
    age = int(input())
    vote (age)
    

if __name__ == "__main__":
    main()
