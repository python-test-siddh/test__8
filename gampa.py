import fputs
fputs.__doc__
fputs.__name__
fputs.fputs("Real Python!", "write.txt")


with open("write.txt", "r") as f:
    print(f.read())
