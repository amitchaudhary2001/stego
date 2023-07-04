file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/full.txt'  # Replace with the actual file path

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Get the length of the file contents
file_length = len(file_contents)

# Print the length of the file
print(f"The length of the file is: {file_length} characters.")