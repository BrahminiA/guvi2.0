def leastFrequent(arr, n) :
	arr.sort()
	min_count = n + 1
	res = -1
	curr_count = 1
	for i in range(1, n) : 
		if (arr[i] == arr[i - 1]) : 
			curr_count = curr_count + 1
		else : 
			if (curr_count < min_count) : 
				min_count = curr_count 
				res = arr[i - 1] 
			
			curr_count = 1
	if (curr_count < min_count) : 
		min_count = curr_count 
		res = arr[n - 1] 
	
	return res
k=int(input())
arr = list(map(str,input().split()))
n = len(arr) 
print(leastFrequent(arr, n)) 


