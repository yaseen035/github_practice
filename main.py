import os

# Print details of dirctory
print("Current Directory:", os.getcwd())
print("List of files and directories in current directory:", os.listdir())

# Create a new directory
new_dir = "new_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:    print(f"Directory '{new_dir}' already exists.")

# Change to the new directory
os.chdir(new_dir)
print("Changed to new directory:", os.getcwd())

# Create a new file in the new directory
file_name = "example.txt"
with open(file_name, 'w') as file:
    file.write("This is an example file.")
print(f"File '{file_name}' created in '{new_dir}'.")