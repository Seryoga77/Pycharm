def all_variants(text):
    n = len(text)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield text[start:end]

# Пример использования генератора
a = all_variants("abc")
for variant in a:
    print(variant)
    