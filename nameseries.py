import os

dataset = input("path: ")
key = input("key: ")

if not os.path.exists(dataset):
    print("path not found")
    exit()

nfile = 0

for item in os.listdir(dataset):
    if os.path.isfile(dataset + "/" + item):
        ftype = os.path.splitext(item)[1]
        os.rename(dataset + "/" + item, dataset + "/" + key + str(nfile) + ftype)
        nfile = nfile + 1

print("renamed the contents successfully")