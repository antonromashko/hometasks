
f = open("myfile.txt", "r+")

f.seek(0,2)
length = f.tell()
print(f"LEN: {length}")
f.seek(0,0)

steps = round(length / 2)

for i in range(steps):
    print(i, length-i)
    f.seek(i, 0)
    pos = f.tell()
    left = f.read(1)
    f.seek(length-i, 0)
    right = (f.read(1))

    f.seek(length-i, 0)
    f.write(left)

    f.seek(i, 0)
    f.write(right)

f.close()