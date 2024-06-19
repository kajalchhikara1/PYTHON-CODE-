#Write a program that reads the content of a text file and prints it to the console.

try:
    with open("text.txt", 'r') as f:
        s = f.read()
        print("Content of file is:\n", s)
        print("File successfully read!")
except Exception as e:
    print(f"Exception {e} has occurred")

