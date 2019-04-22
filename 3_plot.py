from searchAlgo import LinearSearch
from searchAlgo import BinarySearch
import random
from time import time
import matplotlib.pyplot as plt

n=10000
linearTimeArr =[]
binaryTimeArr=[]
sizeArr =[]

# Linear Search
for i in range(n,n*11,n):
	sizeArr.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	LinearSearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	linearTimeArr.append(totalTime)
	print("Linear search for last value in size",i,"is",totalTime)

# Binary Search
for i in range(n,n*11,n):
	randomvalues = random.sample(range(i), i)
	startTime = time()
	randomvalues.sort()
	BinarySearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	binaryTimeArr.append(totalTime)
	print("Binary search for last value in size",i,"is",totalTime)

# Plot size vs time graph
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArr,linearTimeArr, label = 'Linear Search')
ax.plot(sizeArr,binaryTimeArr, label = 'Binary Search')
legend = ax.legend(loc = 'upper center', fontsize = 'large')
plt.show()

