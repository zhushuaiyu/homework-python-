import random

a = []
for i in range(0, 10):
    out = random.randint(10, 50)
    a.append(out)
fi = open('1.3.txt', 'w')
with fi as f:
    for i in a:
        out = i
        out = str(out)
        out = out, '\n'
        f.writelines(out)
print('The content of the file is：')

with open('1.3.txt', 'r') as f:
    f.seek(0, 0)
    print(f.read())
