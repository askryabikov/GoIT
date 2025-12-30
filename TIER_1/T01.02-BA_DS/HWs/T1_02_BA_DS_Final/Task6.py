items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}



def greedy_algorithm(items, budget):
    """
    Жадібний підхід:
    1. Рахуємо співвідношення calories / cost
    2. Сортуємо страви за цим співвідношенням (спадання)
    3. Беремо страви, поки вистачає бюджету
    Повертає: (total_calories, spent_budget, chosen_items)
    """
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    # Перетворюємо словник у список (name, data)
    items_list = list(items.items())

    # Сортуємо за ratio = calories / cost (від більшого до меншого)
    items_list.sort(key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    # Жадібно додаємо страви
    for name, data in items_list:
        cost = data["cost"]
        calories = data["calories"]

        if cost <= remaining_budget:
            chosen_items.append(name)
            remaining_budget -= cost
            total_calories += calories

    spent_budget = budget - remaining_budget
    return total_calories, spent_budget, chosen_items


def dynamic_programming(items, budget):
    """
    Динамічне програмування (0/1 knapsack):
    кожну страву можна взяти або не взяти (максимізація калорій при обмеженому бюджеті)

    dp[i][b] = максимум калорій, використовуючи перші i страв і бюджет b

    Повертає: max_calories, spent_budget, chosen_items
    """
    item_names = list(items.keys())
    n = len(item_names)

    # Таблиця dp: (n+1) рядків і (budget+1) колонок
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо dp знизу вгору
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            # Варіант 1: не беремо цю страву
            dp[i][b] = dp[i - 1][b]

            # Варіант 2: беремо цю страву (якщо бюджет дозволяє)
            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    # Відновлюємо вибрані страви (backtracking)
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            chosen_items.append(name)
            b -= items[name]["cost"]

    chosen_items.reverse()

    max_calories = dp[n][budget]
    spent_budget = budget - b
    return max_calories, spent_budget, chosen_items


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy result:", greedy_result)
    print("DP result:", dp_result)