from os import walk

# Print files recursively

# folder path
dir_path = r'~'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)
