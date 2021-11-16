def binarySearch(nums, target):
        
  # initializing pointer for index access
        
  pointerStart = 0
  pointerEnd = len(nums)-1

  # conditional statement (Execute code until condition is met)
              
  while pointerStart <= pointerEnd:
    #Midpoint is set to be half of the searched portion of the list
    midpoint = (pointerStart + pointerEnd) // 2
    #If condition holds, search is done return midpoint
    if nums[midpoint] == target:
      return (f'The target {target} was found at index {midpoint}')
    #only look at the elements after the midpoint   
    elif nums[midpoint] < target:
      pointerStart = midpoint + 1 
    #only look at the elements before the midpoint            
    else:
      pointerEnd = midpoint-1
  #If done traversing through list, pointerstart is greater that pointerEnd , return            
  return ((f'The target {target} was found not found in this list'))

print(binarySearch([1,2,3,45,67], 5))