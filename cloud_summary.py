from providers import make_client
import json

TEXT = """
Одеський державний університет відновив свою роботу в Одесі 21 квітня 1944 року.
У 1945 році йому було присвоєно ім’я І. І. Мечникова.
У 1965 році університет був нагороджений орденом Трудового Червоного Прапора.
У 1978 році його включили до переліку провідних університетів СРСР.
До кінця 1980-х років університет складався з 9 факультетів.
У 2020 році Одеський національний університет імені І. І. Мечникова відзначив 155-річчя від заснування.
"""

PROMPT = (
    "Стисни наступний текст до двох речень, збережи всі числа:\n\n"
    + TEXT
)

client, model = make_client("cloud")

answers = []

for attempt in range(2):
    print(
        f"{model} / 3_summary / спроба {attempt + 1} "
        "— виконується..."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=0.7,
        max_tokens=1500,
    )

    answer = response.choices[0].message.content
    answers.append(answer)

    print(
        f"{model} / 3_summary / спроба {attempt + 1} "
        "— готово"
    )

with open(
    "cloud_summary.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        {"3_summary": answers},
        f,
        ensure_ascii=False,
        indent=2
    )

print()
print("ГОТОВО!")
print("Результати збережено у cloud_summary.json")