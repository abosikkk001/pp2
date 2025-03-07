import os

def check_access(path):
    print("Path exists:", os.access(path, os.F_OK))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

check_access("test.txt")