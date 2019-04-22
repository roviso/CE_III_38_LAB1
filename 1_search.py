arr=[]

def LinearSearch(values,target):
    n=len(values)
    for i in range(n):
    	if values[i]==target:
        	return i
    return -1  

def BinarySearch(values,target):
	first = 0
	last=len(values)-1
	index= -1
	while first<=last and index==-1:
		midPoint = (first+last)//2
		if(values[midPoint] == target):
			index= midPoint
		else:
			if(values[midPoint]>target):
				last = midPoint-1
			else:
				first = midPoint+1
	return index

if __name__=="__main__":
	print("Input numbers to add to list and any other character to finish")
	# To take only integer values
	while True:
		try:
			x=input("Input Number:")
			x=int(x)
			arr.append(x)
		except:
			break

	print(arr)
	searchVal = int(input("Input the values to be searched from the above list:"))

	linSearchVal = LinearSearch(arr,searchVal)

	if(linSearchVal==-1):
		print("The value",searchVal,"doesn't exist in the list")
	else:
		print("The value lies in ",linSearchVal,"according to Linear Search")

	arr.sort()
	binSearchVal = BinarySearch(arr,searchVal)

	if(binSearchVal==-1):
		print("The value",searchVal,"doesn't exist in the list")
	else:
		print("The value lies in ",binSearchVal,"according to Binary Search in sorted data")
