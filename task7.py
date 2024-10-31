import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    probabilities = {sum_val: (count / num_rolls) * 100 for sum_val, count in sums_count.items()}
    return probabilities

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

num_rolls = 1000000
monte_carlo_probabilities = simulate_dice_rolls(num_rolls)

print("Ймовірності для кожної суми (Метод Монте-Карло):")
for sum_val in range(2, 13):
    print(f"Сума: {sum_val}, Імовірність: {monte_carlo_probabilities[sum_val]:.2f}% (Аналітична: {analytical_probabilities[sum_val]}%)")

sums = list(monte_carlo_probabilities.keys())
mc_values = list(monte_carlo_probabilities.values())
analytical_values = [analytical_probabilities[sum_val] for sum_val in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, mc_values, width=0.4, label="Метод Монте-Карло", align="center", color='skyblue')
plt.plot(sums, analytical_values, marker='o', color='orange', label="Аналітичні значення", linewidth=2)
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірність сум при киданні двох кубиків")
plt.legend()
plt.grid(axis='y')
plt.show()