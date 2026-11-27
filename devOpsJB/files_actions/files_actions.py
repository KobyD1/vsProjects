import os

folder_name = "os_demo_dir"
os.makedirs(folder_name, exist_ok=True)
files = os.listdir(folder_name)

old_file = os.path.join(folder_name, "draft.txt")
new_file = os.path.join(folder_name, "final.txt")

with open(old_file, "w", encoding="utf-8") as f:
  f.write("Sample content\n")

if os.path.exists(new_file):
  os.remove(new_file)

os.rename(old_file, new_file)

print("Files in folder:", os.listdir(folder_name))