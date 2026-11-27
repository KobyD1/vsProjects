def human_size(size):
    new_size= size/(10**12)
    new_size = round(new_size,2)
    return new_size

import shutil

total, used, free = shutil.disk_usage("/")

print(f"Total: {human_size(total)}Tbit")
print(f"Used: {human_size(used)}Tbit")
print(f"Free: {human_size(free)}Tbit")


