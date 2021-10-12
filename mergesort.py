def merge_sort(list, left_index, right_index):  
    if left_index >= right_index:  
        return  
  
    middle = (left_index + right_index)//2  
    merge_sort(list, left_index, middle)  
    merge_sort(list, middle + 1, right_index)  
    merge(list, left_index, right_index, middle)  
  
    
def merge(list, left_index, right_index, middle):  
  
    left_sub = list[left_index:middle + 1]  
    right_sub = list[middle+1:right_index+1]  
  
    left_sub_index = 0  
    right_sub_index = 0  
    sorted_index = left_index  
 
    while left_sub_index < len(left_sub) and right_sub_index < len(right_sub):  
    
        if left_sub[left_sub_index] <= right_sub[right_sub_index]:  
            list[sorted_index] = left_sub[left_sub_index]  
            left_sub_index = left_sub_index + 1   
        else:  
            list[sorted_index] = right_sub[right_sub_index]  
            right_sub_index = right_sub_index + 1  
  
        sorted_index = sorted_index + 1  
  
    while left_sub_index < len(left_sub):  
        list[sorted_index] = left_sub[left_sub_index]  
        left_sub_index = left_sub_index + 1  
        sorted_index = sorted_index + 1  
  
    while right_sub_index < len(right_sub):  
        list[sorted_index] = right_sub[right_sub_index]  
        right_sub_index = right_sub_index + 1  
        sorted_index = sorted_index + 1  
  
list = [32,-23,43,65,190,90]  
merge_sort(list, 0, len(list) -1)  
print(list)