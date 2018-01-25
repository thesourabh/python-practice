def mergesort (A):
	n = len(A)
	if (n < 2):
		return A
	mid = n // 2
	return merge(mergesort(A[:mid]), mergesort(A[mid:]))

def merge(B, C):
	len_B = len(B)
	len_C = len(C)
	i = 0
	j = 0
	merged = []
	while (i < len_B) and (j < len_C):
		if (B[i] <= C[j]):
			merged.append(B[i])
			i += 1
		else:
			merged.append(C[j])
			j += 1
	if (i < len_B):
		merged += B[i:]
	if (j < len_C):
		merged += C[j:]
	return merged
	

print(mergesort([6,4,9,3,2,1]))