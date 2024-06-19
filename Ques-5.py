#Write a program that takes a string input from the user and writes it to a text file.

str= input("Enter a string ")
try:
    f = open("text","w")
    f.write(str)
    print("String successfully added")
except Exception as e:
    printf(f"An error occured: {e}")
    
