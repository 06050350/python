def score_threshold(l,t):
	Ans=[]
	for i in range(len(l)):
		if(l[i]>=t):
			Ans.append(True)
		else:
			Ans.append(False)
    

	return Ans
print(score_threshold([56, 72, 98, 11, 34, 99], 60))