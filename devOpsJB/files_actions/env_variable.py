import os

name = os.getenv("MY_NAME", "Guest")

print(f"Hello {name}")
# need to define before Env. variables by 
# windows (power shell) - 
# $env:MY_NAME="Wolrd"
# LINUX/MAC 
# export MY_NAME="Wolrd"

