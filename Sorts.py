def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        temp = nums[min_index]
        nums[min_index] = nums[i]
        nums[i] = temp

a = [34,55,12,23,65,99]
selection_sort(a)
print(a)
    
def insertion_sort(nums):
    for i in range(1,len(nums)):
        val = nums[i]
        j = i-1
        while j >=0 and val < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = val

b = [34,55,12,23,65,99]
insertion_sort(b)
print(b)

def merge_sort(nums):
    if len(nums) > 1:
        middle  = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j] :
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

c = [34,55,12,23,65,99]
insertion_sort(c)
print(c)

def bubble_sort(nums):
    size = len(nums)
    for i in range(size):
        for j in range(0,size-i-1):
            if nums[j] > nums [j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

d = [34,55,12,23,65,99]
insertion_sort(d)
print(d)