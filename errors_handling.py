def get_valid_filename ():
    """Function check for a valid file name """

    while True:
        try:
            filename = input("Please enter the filename: ")

            # Read the file
            with open(filename, 'r', encoding="utf-8") as f:
                print(f"Success! The '{filename}' was found")

            return filename
        
        except FileNotFoundError:
            print(f"Error: '{filename}' could not be found")

if __name__ == "__main__":
    valid_file = get_valid_filename()
    if valid_file:
        print(f"Chopsen file: '{valid_file}'. Process completed.")