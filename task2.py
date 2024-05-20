import heapq

def merge_k_lists(lists):
    # Створюємо мін-купу
    heap = []
    
    # Додаємо перший елемент з кожного списку в купу разом з індексами списку та елемента
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # перевіряємо, чи список не порожній
            heapq.heappush(heap, (sorted_list[0], i, 0))
    
    result = []
    
    while heap:
        # Виймаємо найменший елемент з купи
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Якщо в цьому списку залишилися елементи, додаємо наступний елемент у купу
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
    
    return result

# Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
