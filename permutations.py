def permutations(list, arr=[], res=[]):
	if len(arr) == len(list):
		res.append(arr)
	else:
		for i in range(0, len(list)):
			if list[i] not in arr:
				permutations(list, arr + [list[i]], res)
	return res


