#Functin Defination
def modify_file_content(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    """
    try:
        # Opening the input file and read its content
        with open(input_filename, 'r') as fileToProcess:
            content = fileToProcess.readlines()
        
        # Modifying the file - convert each line to uppercase
        modified_content = [line.upper() for line in content]
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as fileToOutput:
            fileToOutput.writelines(modified_content)
        
        #Print the modified file
        print(f"Modified Content in '{output_filename}'.")

    # Handling file errors
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for trying the program")

# Main program
print("Welcome to the File Modifier!")

# Asking the user for the input and output file names
input_file = input("Enter name of the file to read: ")
output_file = input("Enter name of file to add modified content to: ")

#Function call
modify_file_content(input_file, output_file)
