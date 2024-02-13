def linearSearch(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i


arr = [1, 2, 13, 4, 7, 9]
target = 7

print(linearSearch(arr, target))
