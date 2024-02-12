# 1) Problem statement
# 2) Constraints
# 3) Examples

# NAIVE APPROACH


def naive_(arr):
    for i in range(len(arr)):
        # keep the current element fixed
        is_single_num = 1
        # flag element is to check if we meet a double number 
        for j in range(len(arr)):
            # check for double number
            if i != j and arr[i] == arr[j]:

                is_single_num = 0
                break
        
        if is_single_num == 1:
            return i


def searching_sorting(arr):
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i+1]:
                return i
        
        elif i == len(arr) - 1:
            if arr[i] != arr[i - 1]:
                return i
        
        else:
            if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                return i


def hashmap(arr):
    ref_dict = dict()
    for i in range(len(arr)):
        if arr[i] not in ref_dict:
            ref_dict[arr[i]] = 1
        else:
            ref_dict[arr[i]] += 1

    
    for key, value in ref_dict.items():
        if value == 1:
            return key


arr = [2,-1,2,-1,-4]
index = searching_sorting(arr)

# print(arr[index])

print(hashmap([2, 1, 2, 7, 4, 7, 1]))
