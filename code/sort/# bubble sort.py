# bubble sort
def bubblesort(arr0):
    for i in range(len(arr0)):
        for j in range(len(arr0) - i - 1):
            if arr0[j] > arr0[j + 1]:
                arr0[j], arr0[j + 1] = arr0[j + 1], arr0[j]
    return arr0


if __name__ == "__main__":
    print(bubblesort([5, 4, 3, 2, 1]))
