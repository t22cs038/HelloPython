def quick_sort(data):
    
    if len(data) <= 1:
        return data
    
    pivot = data.pop(0)
    
    left = [i for i in data if i <= pivot]
    
    right = [i for i in data if i > pivot]
    
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right

Data = [6,2,7,11,14,12,9]

print(Data,quick_sort(Data[:]))
