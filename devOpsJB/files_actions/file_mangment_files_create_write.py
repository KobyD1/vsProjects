import os

original_dir = os.getcwd()
folder_name = "os_demo_dir"
os.makedirs(folder_name, exist_ok=True)
print("Directory created at:", os.path.abspath(folder_name))

#   Change into the directory
os.chdir(folder_name)
print("Current working directory:", os.getcwd())

#  Create empty file in  directory
file_name = "notes.txt"
open(file_name, "w", encoding="utf-8").close()

#  create file with text 
file_text_name = "notes_with_text.txt"

with open(file_text_name, "w", encoding="utf-8") as f:
    f.write(f"Sample Example content for {file_name}\n")

#  read file text , with is not mandatory , without with it did not closed 

with open(file_text_name, "r", encoding="utf-8") as f:
  content = f.read()
  f.close()     # close allready auto done by with open   

  print(f"file content {content}")








