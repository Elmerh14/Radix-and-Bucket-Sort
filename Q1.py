import numpy as np
import heapq

def countingSort(arr):
    if not arr:
        return arr
    
    minVal = min(arr)
    maxVal = max(arr)
    rangeVal = maxVal - minVal + 1

    count = [0] * rangeVal
    output = [0] * len(arr)

    for num in arr:
        count[num - minVal] += 1

    for i in range(1, len(count)):
        count[i] += count[i -1]

    for i in reversed(range(len(arr))):
        num = arr[i]
        count[num - minVal] -= 1
        output[count[num - minVal]] = num

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

def radixSortWithCountingSort(arr):
    maxVal = max(arr)
    exp = 1
    
    while maxVal // exp > 0:
        radixArray = [[] for _ in range(10)]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            if bucket:
                countingSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

def bucketSort(arr):
    minVal, maxVal = min(arr), max(arr)
    totalBuckets = len(arr)
    buckets = [[] for _ in range(totalBuckets)]

    for val in arr:
        bucketNumber = int(totalBuckets * (val - minVal) / (maxVal + 1))
        buckets[bucketNumber].append(val)

    arr.clear()
    for bucket in buckets:
        arr.extend(sorted(bucket))

    return arr

def mergKsortedList(arr):
    heap = []
    result = []
    for i in range(len(arr)):
        if len(arr[i]) > 0:
            heapq.heappush(heap, (arr[i][0], i, 0))

    while heap:
        value, arrIndex, elemenIndex = heapq.heappop(heap)
        result.append(value)

        if elemenIndex + 1 < len(arr[arrIndex]):
            nextValue = arr[arrIndex][elemenIndex + 1]
            heapq.heappush(heap, (nextValue, arrIndex, elemenIndex + 1))
        
    return result
            



def main():
    with open("rand1000000.txt") as file:
        list = [int(num) for line in file for num in line.split()]
        #use numpy to split the list of integers into 100 subarrays 
        splitList = np.array_split(list,100)
        #convert the numpay arrays into regular array's
        flatList = [arr.tolist() for arr in splitList]

        #iterate over the arrays elements 0-50 and sort with radix sort
        for i in flatList[:len(flatList)//2]:
            radixSortWithCountingSort(i)

        #iterate over arrays elements 50-100 and sort using bucket sort
        for i in flatList[len(flatList)//2:]:
            bucketSort(i)

        #merge all of these subbarrays into on single list
        mergedList = mergKsortedList(flatList)

        print(mergedList[:100])

            



if __name__ == "__main__":
    main()