import random


def main():
	print(generate_X(6000))

def generate_X(n):
	count = 0
	perm = [6, 7, 2, 5, 1, 4,3 ]
	for i in range(0,n):
		sim = generate_random(7)
	return count

def generate_random(count):
	xarray[]
	xdict{}
	for j in range(1, count+1):
		x = random.randint(0,1000)/1000
		xarray.append(x)
		xdict[x] = j
	xarray.sort()
	jarray = []
	for k in range(0,count):
		jarray.append(xdict[xarray[count-1-k]])
	return jarray

if __name__ == "__main__":
	main()