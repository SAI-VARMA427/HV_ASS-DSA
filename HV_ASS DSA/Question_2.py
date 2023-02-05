def unique_elements(arr):
  arr.sort() 
  unique_list = [] 
  for i in range(len(arr)):
    if i == 0 or arr[i] != arr[i - 1]:
      unique_list.append(arr[i]) 
  return unique_list


arr = [5, 4, 7, 5, 1, 3, 4]
print(unique_elements(arr))
