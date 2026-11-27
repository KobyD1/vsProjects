
import os


folder = "os_demo_dir"
os.makedirs(folder, exist_ok=True)

filenames = ["file1.txt", "file2.txt", "file3.log"]

for name in filenames:
  file_path = os.path.join(folder, name)
  with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"Content for {name}\n")

print("Created files:", os.listdir(folder))