def swap(A, i, j):
	temp = A[j]
	A[j] = A[i]
	A[i] = temp


def quicksort(A, start, end):
	if (start < end):
		p_index = partition(A, start, end)
		print(start, end, p_index, A)
		quicksort(A, start, p_index - 1)
		quicksort(A, p_index + 1, end)
	
def partition(A, start, end):
	pivot = A[end]
	p_index = start
	for i in range(start, end):
		if A[i] < pivot:
			swap(A, i, p_index)
			p_index += 1
	swap(A, p_index, end)
	return p_index

	
A = [6,4,9,3,2,1,5]
quicksort(A, 0, len(A) - 1)
print(A)