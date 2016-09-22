import random


def main():
	generate_X()

def generate_X():
	count = 0
	perm = [6, 7, 2, 5, 1, 4,3 ]
	for i in range(0,6000):
		xarray = []
		xdict = {}
		for j in range(1,8):
			x = random.randint(0,1000)/1000
			xarray.append(x)
			xdict[x] = j
		xarray.sort()
		jarray = []
		for k in range(0,7):
			jarray.append(xdict[xarray[6-k]])
		if jarray == perm:
			count = count + 1
	print(count)


if __name__ == "__main__":
	main()