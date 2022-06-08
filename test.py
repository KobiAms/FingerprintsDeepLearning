


with open('./test.txt', 'r') as outfile:
    x = outfile.read()
    x = x.split('\n')
    for xi in x:
        print(xi, 'X')