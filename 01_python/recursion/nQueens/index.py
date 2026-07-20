n = 8
# arr = ['.', '.', '.', '.']
# for i in range(n):
arr = []

for i in range(n):
    a = []
    for i in range(n):
        a.append('.')
    arr.append(a)

def printArr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
        # print(i)



def isValid(arr, row, col):
    i = row
    j = col
    while (i >= 0 and j >= 0):
        if (arr[i][j] == "Q"):
            return False
        i-= 1
        j-=1
    i = row
    j = col
    while (i >= 0 and j < n):
        if (arr[i][j] == "Q"):
            return False
        i -= 1
        j += 1
    i = row
    j = col
    while (i >= 0):
        if (arr[i][j] == "Q"):
            return False
        i -= 1
    return True

def solve(arr, row):
    if (row >= n):
        print("--------------------------solutions --------------------")
        printArr(arr)
        return
    for i in range(n):
        if (isValid(arr, row, i)):
            arr[row][i] = "Q"
            solve(arr, row + 1)
            arr[row][i] = "."

solve(arr, 0)
