

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for res in a:
    if res < 5:
        print(res)

print([elem for elem in a if elem < 5])