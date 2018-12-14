

data = list(range(100))

with open('jeff.txt', 'w') as f:
    f.write("---------------------- \n")
    for row in data:
        f.write(str(row) + "\n")
