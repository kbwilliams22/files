import os


def main():
    while True:
        try:
            get_pth()
            read_file()
            menu()
        except FileNotFoundError:
            print("File not found. Please select '2' to create a new file or select a valid file.")
            menu()
        except:
            print("\nAn error occurred. Please make a choice.")
            menu()
        break


#User enters info to be appended to selected file
def info():
    name = input("Please type your name: ")
    if (len(name) == 0):
        print("Note: Text field empty. No name will be added.")
    addr = input("Please type your address: ")
    if (len(addr) == 0):
        print("Note: Text field empty. No address will be added.")
    num = input("Please type your phone number: ")
    if (len(num) == 0):
        print("Note: Text field empty. No number will be added.")
    return name, addr, num


#Gets directory name from user, creates directory if name is not found
def get_pth():
    pth = input("Name of directory: ")
    if (len(pth) == 0):
        print("Text field empty. Please enter a value.")
        main()
    if not os.path.exists(pth):
        print("\nDirectory does not exist. Creating directory ", "'", pth, "'.\n", sep="")
        os.mkdir(pth)
    else:
        print("\nYou entered: ", pth, "\n")
        pass
    os.chdir(pth)
    return pth


#Gets file name from user, creates file if name is not found
def get_file():
    file = input("Name of file: ")
    print("\nYou entered: ", file, "\n")
    if (len(file) == 0):
        print("text field empty, a file named '.txt' will be created.")
    print('''Please note: All created files will end with .txt so that they can be edited! 
             This will be done automatically if not specified in the name.\n''')
    os.path.splitext(file)

    if file.split('.')[-1] != "txt":
        file = file + ".txt"
    return file


#Appends user's text to selected file
def append():
    file = get_file()
    name, addr, num = info()
    f = open(file, "a")
    f.write(name + ", " + addr + ", " + num + "\n")
    f.close()
    return file


#Outputs file contents
def read_file():
    file = append()
    print("\nText in file:")
    print(open(file).read())


#Outputs file contents without other functions
def menu_read():
    file = get_file()
    print(file)
    print(open(file).read())


#Menu for choosing what to do after the program ends. Found on stack overflow:
#https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
def menu():
        ans = True
        while ans:
            print("""
            1. Create/Select directory
            2. Create/Edit file
            3. Read contents of file
            4. Exit/Quit
            """)
            ans = input("What would you like to do? ")
            if ans == "1":
                print("\n")
                get_pth()
                menu()
            elif ans == "2":
                print("\n")
                append()
                menu()
            elif ans == "3":
                print("\n")
                menu_read()
                menu()
            elif ans == "4":
                print("\n Exiting...")
            else:
                print("\nInvalid input. Please try again.")
                menu()
            return ans


if __name__ == "__main__":
    main()