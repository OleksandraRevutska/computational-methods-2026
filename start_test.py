import time
from providers import make_client

client, model = make_client("local")

prompt = "Столиця Франції?"

t_start = time.perf_counter()
first_token_at = None
parts = []

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)

for chunk in stream:
    piece = chunk.choices[0].delta.content

    if piece:
        if first_token_at is None:
            first_token_at = time.perf_counter()

        parts.append(piece)

t_end = time.perf_counter()

print("Відповідь:", "".join(parts))
print(f"TTFT: {first_token_at - t_start:.3f} с")
print(f"Всього: {t_end - t_start:.3f} с")