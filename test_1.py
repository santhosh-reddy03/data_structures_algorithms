# num = int(input())

# a = []
# for i in range(1,num):
# 	temp = i*(i+1)/2
# 	if temp > num:
# 		break
# 	else:
# 		a.append(temp)
# for i in range(len(a)):
# 	if num - a[i] in a:
# 		print("yes")
# 		break
# 	elif i == len(a)-1:
# 		print("no")

def polly(x):
	for i in range(len(x)):
		if x[i] == x[-(i+1)]:
			if i == len(x)-1:
				return "yes"
		else:
			return "no"


n = int(input())
for i in range(n):
	st = input()
	print(polly(st))
