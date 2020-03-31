def longest_str(l):
	index=0
	max=len(l[0])
	for i in range(len(l)):
		if(max<len(l[i])):
			index=i
	return l[index]
print(longest_str(['Jane', 'Peter', 'stephanie']))