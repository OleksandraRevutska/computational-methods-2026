from openai import OpenAI
import json

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

model = "qwen3:4b"

TEXT = """
Одеський державний університет відновив свою роботу в Одесі 21 квітня 1944 року.
У 1945 році йому було присвоєно ім’я І. І. Мечникова.
У 1965 році університет був нагороджений орденом Трудового Червоного Прапора.
У 1978 році його включили до переліку провідних університетів СРСР.
До кінця 1980-х років університет складався з 9 факультетів.
У 2020 році Одеський національний університет імені І. І. Мечникова відзначив 155-річчя від заснування.
"""

TASKS = {
    "1_fact":
        "У якому році засновано Одеський національний університет "
        "імені І. І. Мечникова? Відповідай лише роком. /no_think",

    "2_format":
        "Подай дані про Одеський національний університет імені "
        "І. І. Мечникова у JSON з полями name, year, city. "
        "Без пояснень, без markdown, лише JSON. /no_think",

    "3_summary":
        "Стисни наступний текст до двох речень, збережи всі числа:\n\n"
        + TEXT + "\n/no_think",

    "4_code":
        "Напиши функцію is_palindrome(s), яка перевіряє, чи є рядок "
        "паліндромом, ігноруючи пробіли й регістр. Лише код. /no_think",

    "5_logic":
        "У групі 25 студентів, 12 знають Python, 9 знають Java, "
        "4 знають обидві мови. Скільки студентів не знають жодної "
        "з цих мов? Покажи хід розв'язання. /no_think",

    "6_language":
        "Чим стек відрізняється від черги? "
        "Поясни українською, два абзаци. /no_think",
}

results = {}

for task_id, prompt in TASKS.items():

    answers = []

    for attempt in range(2):

        print(
            f"{model} / {task_id} / спроба {attempt + 1} "
            "— виконується..."
        )

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
        )

        answer = response.choices[0].message.content

        answers.append(answer)

        print(
            f"{model} / {task_id} / спроба {attempt + 1} "
            "— готово"
        )

    results[task_id] = answers

    # Зберігаємо після кожного завдання
    with open(
        "qwen_quality.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            results,
            f,
            ensure_ascii=False,
            indent=2
        )

print()
print("ГОТОВО!")
print("Результати збережено у qwen_quality.json")