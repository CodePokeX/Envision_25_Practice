# Make sure the program prints the string correctly

def main():
    # Printing all the characters in an array
    z = ['h', 'e', 'l', 'l', 'o', '!']
    
    new = ""
    
    for i in range(6):
        new += z[i]
    
    for i in range(6):
        print(new[i], end="")
    print()


if __name__ == "__main__":
    main()
