from collections import Counter
n=int(input())
lst = list(map(str,input().split()))

counts = Counter(lst)
new_list = sorted(lst, key=counts.get, reverse=True)
print (lst[len(lst)-1]) 
