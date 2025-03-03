

x = 3
y = 6


def add(x,y):
    print("Starting Addition")
    return x + y

def sub(x,y):
    print("Starting Subtarction")
    return x - y

print(add(x,y))
print(sub(x,y))

z = x + y

if z % 3 == 0:
    print("z value is even")
    if z > 3:
        print("z value greater than 6")
else:
    print("z is an odd number")