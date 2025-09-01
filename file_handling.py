# Answer for question 1

def modify_file(input_file, output_file):
    try:
        # Step 1: Read the content of the input file
        with open(input_file, "r") as infile:
            content = infile.read()

        # Step 2: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 3: Write the modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_file}")

  #Answer for question 2
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main program
if __name__ == "__main__":
    # Ask the user for the filename
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = "modified_" + input_file  # create new file with prefix

    modify_file(input_file, output_file)
