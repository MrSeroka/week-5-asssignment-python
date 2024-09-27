from math import e


with open("my_file.txt", "w") as file:

    file.write("This is the first line of text.\n"),

file.write("The second line has a number: 42.\n"), # String with a number

file.write("3.14159 is the value of pi.\n"),

print("Text written to my_file.txt successfully."),

with open("my_file_.txt", "r") as file:

    contents = file.read()

    print ("\nContents of my_file.txt:")
    print(contents)

    with open("my_file.txt", "a") as file: 

        file.write("This is an additional line 1.\n")  
    file.write("Another line with a number: 100.\n")  # Additional string with a number
    file.write("Last line with some text.\n")  # Additional string

print("Additional lines appended to my_file.txt successfully.")


with open("my_file.txt", "r") as file: 

    contents = file.read() 
    print("\nContents of my_file.txt:")
    print(contents)
 
    except FileNotFoundError :
    print("Error: The file was not found.")
    
    except PermissionError:
    print("Error: You do not have permission to access this file.")
    
    except Exception as e:
    print(f"An unexpected error occurred: {e}")
        
    finally: 
    print("\nExecution of file handling operations complete.")