import matplotlib.pyplot as plt

labels = [
    "Локальна\nкороткий",
    "Локальна\nсередній",
    "Локальна\nдовгий",
    "Хмарна\nкороткий",
    "Хмарна\nсередній",
    "Хмарна\nдовгий"
]

speed = [
    11.4,
    39.9,
    32.6,
    65.9,
    652.6,
    1083.8
]

plt.figure(figsize=(11, 6))

bars = plt.bar(labels, speed)

plt.title("Швидкість генерації локальної та хмарної моделей")
plt.xlabel("Модель та тип промпту")
plt.ylabel("Швидкість, символів/с")

for bar, value in zip(bars, speed):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10,
        str(value),
        ha="center"
    )

plt.tight_layout()

plt.savefig("speed_chart.png", dpi=300)

plt.show()