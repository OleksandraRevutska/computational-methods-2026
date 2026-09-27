import time
from providers import make_client

QUESTION = "Поясни різницю між списком і кортежем у Python. Коротко."

for name in ["local", "cloud"]:
    client, model = make_client(name)

    t0 = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": QUESTION}
        ],
        temperature=0.7,
    )

    elapsed = time.perf_counter() - t0
    text = response.choices[0].message.content

    print(f"===== {name.upper()} ({model}) =====")
    print(text)
    print(f"Час: {elapsed:.2f} с")
    print(f"Довжина відповіді: {len(text)} символів")
    print(response.usage)
    print()