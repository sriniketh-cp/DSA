def navive(arr):
    for i in range(arr):
        singlecount=0
    for j in range(arr):
        if(arr[i]==arr[j]):
            singlecount=1

        if(singlecount ==1):
            return arr[i];

    return -1;