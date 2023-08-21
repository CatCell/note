# insertsort
def insertsort(arr0):
    for i in range(len(arr0)):
        yespos, nopos = i, i + 1
        for j in range(yespos, -1, -1):
            if arr0[nopos] > arr0[j]:
                temp = arr0[nopos]
                arr0.pop(nopos)
                arr0.insert(j + 1, temp)
                break
            else:
                temp = arr0[nopos]
                arr0.pop(nopos)
                arr0.insert(0, temp)


if __name__ == "__main__":
    print(insertsort([5, 4, 6, 2, 1]))
