def selectionSort(A, reverse=False):

    for i in range(len(A)):
        ind = i
    for j in range(i + 1, len(A)):
        if reverse==False:
            if A[ind] > A[j]:
                ind = j
        else:
            if A[ind] < A[j]:
                ind = j
                A[i], A[ind] = A[ind], A[i]
    return A

print(selectionSort([5,4,6,3,7,2]))
print(selectionSort([5,4,6,3,7,2],True))