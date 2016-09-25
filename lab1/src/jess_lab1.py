import random
import math

def main():
	#print(generate_X(6000))
	average9 = 0
	average21 = 0
	average36 = 0
	average69 = 0
	for i in range(0,10000):
		average9 = average9 + find_first_positionB(9)
		average21 = average21 + find_first_positionB(21)
		average36 = average36 + find_first_positionB(36)
		average69 = average69 + find_first_positionB(69)
	average9 = average9/10000
	average21 = average21/10000
	average36 = average36/10000
	average69 = average69/10000
	print("9 n: ",average9)
	print("21 n: ",average21)
	print("36 n: ",average36)
	print("69 n: ",average69)

	find_first_positionB(9)

def generate_X(n):
	count = 0
	perm = [6, 7, 2, 5, 1, 4,3 ]
	for i in range(0,n):
		sim = generate_random(7)
		if sim == perm:
			count = count + 1
	return count

def generate_random(count):
	xarray=[]
	xdict={}
	for j in range(1, count+1):
		x = random.random()
		xarray.append(x)
		xdict[x] = j
	xarray.sort()
	jarray = []
	for k in range(0,count):
		jarray.append(xdict[xarray[count-1-k]])
	return jarray

def find_first_positionA(n):
	sim = generate_random(n)
	for i in range(0, n):
		if sim[i] == 1:
			return i+1

def find_first_positionB(n):
	sim = generate_random(n)
	found = False
	count = 0
	while (not found):
		halfn = math.floor(n/2)
		count = count + 1
		if len(sim) <= 2:
			return count
		elif 1 in sim[0:halfn]:
			sim = sim[0:halfn]
			n = len(sim)
		else:
			sim = sim[halfn:]
			n = len(sim)


if __name__ == "__main__":
	main()