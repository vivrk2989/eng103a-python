
x = 1
y = 2
print(x, y)


def local_scope():
    x = 500
    y = 700
    return x, y

x, y = local_scope()
print(x, y)


# we can reference the varaible which is outside the fucntion but not assign it