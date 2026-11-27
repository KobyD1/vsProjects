import shutil

python_path = shutil.which("python")
print (f"the path for python is {python_path}")
total, used, free = shutil.disk_usage("/")
terminal = shutil.get_terminal_size

print(total)
print(used)
print(free)