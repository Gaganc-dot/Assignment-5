
def vowel(no1):
    
    if(no1 in 'aeiou'):
        print("'{}'".format(no1), "is a vowel.")
    else:
        print ("'{}'".format(no1),"It's consonant ")


def main():
    print("Enter a character :")
    value1 = input()
    
    vowel (value1)
    

if __name__ == "__main__":
    main()
