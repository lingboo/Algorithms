def recursive_comb(elements, size, left, right, arr=[], res=[]):
	if len(arr) == size:
		res.append(arr)
	else:
		for i in range(left, right):
			recursive_comb(elements, size, i+1, right,
						   arr + [elements[i]], res)
	return res


def combinations(elements, size):
	n = len(elements)
	res = recursive_comb(elements, size, 0, n)
	return res

