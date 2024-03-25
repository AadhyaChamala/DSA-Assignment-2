#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import winsound

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        
        winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
        time.sleep(0.5) 

        print("Merge:", arr)

arr_str = input("Enter space-separated numbers: ")
arr = [int(num) for num in arr_str.split()]

print("Original Array:", arr)
merge_sort(arr)
print("Sorted Array:", arr)


# In[ ]:





# In[ ]:




