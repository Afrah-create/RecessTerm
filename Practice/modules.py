import os
import shutil
'''

cwd = os.getcwd()
print(f"Current working directory: {cwd}")


#nwd = os.chdir("..")
#print(f"New working directory: {os.getcwd()}")


directory = "Afrah2"
parent_dir = os.getcwd()

remove_dir = os.path.join(parent_dir, "Afrah2")
os.rmdir(remove_dir)
print(f"Directory '{remove_dir}' removed.")


path = os.path.join(parent_dir, directory)
print(f"Path to directory: {path}")

os.mkdir(path)
print(f"Directory '{directory}' created at: {path}")


'''


cwd = os.getcwd()
print(f"Current working directory: {cwd}")

file_name = "inputs.py"

file_path = os.path.join(os.getcwd(), file_name)

destination_dir = os.path.join(os.getcwd(), "Afrah2")
shutil.copy(file_path, destination_dir)

#print(os.listdir(parent_dir))

