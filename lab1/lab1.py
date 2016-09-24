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

	hist_X = {}
	hist_Y = {}
	
	for i in range(0, k):
		new_X = generate_X(m)
		array_X.append(new_X)
		if new_X in hist_X:
			hist_X[new_X] = hist_X[new_X] + new_X
		else:
			hist_X[new_X] = 1

		new_Y = generate_Y()
		array_Y.append(new_Y)
		if new_Y in hist_Y:
			hist_Y[new_Y] = hist_Y[new_Y] + new_Y
		else:
			hist_Y[new_Y] = 1

	with open('X.txt', 'w') as f:
		for x in array_X:
			f.write(str(x) + "\n");

	with open('Y.txt', 'w') as f:
		for y in array_Y:
			f.write(str(y) + "\n")

	with open('hist_X.txt', 'w') as f:
		for k, v in hist_X.items():
			f.write(str(k) + " " + str(v) + "\n")
	with open('hist_Y.txt', 'w') as f:
		for k, v in hist_Y.items():
			f.write(str(k) + " " + str(v) + "\n")

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
