r = []
for x in range(10):
    r.append(lambda: x ** 2)

print(r[1](), r[5]())
x = 3
print(r[1](), r[5]())
