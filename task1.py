import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін. купу з кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Об'єднуємо кабелі по два за раз, доки не залишиться один кабель
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо вартість їх з'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Test
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання всіх кабелів:", min_cost_to_connect_cables(cables))
