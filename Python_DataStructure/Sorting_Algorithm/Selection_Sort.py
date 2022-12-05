def Selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1, n): 
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp


a = [5,4,9,6,2]
print("Orginal List:", a)
Selectionsort(a)
print("Sorted List:", a)