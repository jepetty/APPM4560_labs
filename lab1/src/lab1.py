#!/usr/bin/python3
import random
import math

def main():
	n = 7
	m = 6000
	k = 2000
	p = 1 / math.factorial(n)

	array_X = []
	array_Y = []
	
	for i in range(0, k):
		new_X = generate_X(m)
		array_X.append(new_X)
		new_Y = generate_Y()
		array_Y.append(new_Y)
	with open('X.txt', 'w') as f:
		for x in array_X:
			f.write(str(x) + "\n");

	with open('Y.txt', 'w') as f:
		for y in array_Y:
			f.write(str(y) + "\n")

def generate_Y():
	count = 0
	perm = [6, 7, 2, 5, 1, 4, 3]
	found = False
	while not found:
		sim = generate_random(7)
		count = count + 1
		if sim == perm:
			found = True
	return count

def generate_X(n):
	count = 0
	perm = [6, 7, 2, 5, 1, 4, 3]
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

if __name__ == "__main__":
	main()
