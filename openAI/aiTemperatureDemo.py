response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a short poem about the ocean."}],
    temperature=0.7   # controls randomness vs determinism
)
