import os

files = [x for x in os.listdir('.') if x.endswith('.py') and x != "rename.py"]

for src in files:
    dst = src[1:]
    os.rename(src, dst)
