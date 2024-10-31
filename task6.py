items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if budget >= data["cost"]:
            selected_items.append(item)
            budget -= data["cost"]
            total_calories += data["calories"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, data in items.items():
        cost = data["cost"]
        calories = data["calories"]
        
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    max_calories = dp[budget]
    selected_items = item_selection[budget]

    return selected_items, max_calories

budget = 100

selected_greedy, calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_greedy)
print("Загальна калорійність:", calories_greedy)

selected_dp, calories_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", selected_dp)
print("Загальна калорійність:", calories_dp)