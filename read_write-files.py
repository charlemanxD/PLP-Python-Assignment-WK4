import os

def create_file(filename="input.md"):
    """The function create a file"""
    content = [
        "Welcome to PLP Python class.\n",
        "we learned how to read & write to file in Python.\n",
        "We also learned how to handle Exceptions.\n"
    ]

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(content)
    print("File successfully CREATED")

def process_file(input_file= str, output_file = str) -> str:
    """Function Reads, then modifies file and write the result to a new file"""

    try:
        # Open input_file for reading and output_file for writing
        with open(input_file, 'r', encoding="utf-8") as in_file, open(output_file, 'w', encoding="utf-8") as out_file:
            print(f"Reading from '{input_file}' and writing to '{output_file}' ...")

            # Iterate through the lines of text in the input_file
            for line in in_file:
                # Perform modification by capitalizing the text we've itererated through
                modified_lines = line.upper()

                # Write the modification to the output file
                out_file.write(modified_lines)
        print("File processeing completed SUCCESSFULLY ...")
        print(f"Check the '{output_file}' for the result.")
            
    except FileNotFoundError:
        print(f"Error: the '{input_file}' was not found.\n")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    input_file = "input.md"
    output_file = "output.md"

    # Cretae input file if it does not exist
    if not os.path.exists(input_file):
        create_file(input_file)

    process_file(input_file, output_file)
    # End-of-file (EOF)