alist = [54,26,93,17,77,31,44,55,20]
print(alist)
def insertion_sort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index] 
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position -1

        
        alist[position] = currentValue



insertion_sort(alist)
print(alist)
