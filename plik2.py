data = [10, 3, 7, 8, 1, 6, 2, 9, 4, 5, 0]

def sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

sort(data)
print(data)
#zmiana zmiana