def mergeSort(parameter_list):
    print("Spliting ", parameter_list)
    if len(parameter_list) > 1:
        mid = len(parameter_list) // 2
        lefthalf = parameter_list[:mid]
        righthalf = parameter_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                parameter_list[k] = lefthalf[i]
                i=i+1
            else:
                parameter_list[k] = righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            parameter_list[k] = lefthalf[i]
            i=i+1
            k=k+1
    print("Merging ",parameter_list)


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)