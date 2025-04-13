# Comparison Between O(n log k) Algorithm and O(nk) Algorithm

```
The O (n log k) algorithm leverages the speed of the insertion and deletion operations of a minheap. By using a minheap we are able to efficently keep track of the smallest element in our data set. Since we have k list that are already sorted and our heap is kept at most size k. Our inserting and deletion operations lead us with a log k time and since we have n elements our full merging takes O(n log k) time. In comparison to the naive approach which yeilds a O(nk) time complexity we would have to check all k sublisits for the minimum value at each step of the merge. Meaning that we would have to do k comparisons for each of the n elements. This leads us to a slower mergining performance of O(nk)
```