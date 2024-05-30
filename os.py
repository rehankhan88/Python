import os

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(os.getcwd())
    os.chdir("/Users ")
    print(os.listdir(f"Data/{folder}"))
