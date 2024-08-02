from fake_math import divide as fake_divide
from true_math import divide as true_divide

if __name__ == "__main__":
    first = 1
    second = 0


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(f"Результат деления в fake_math: {result1}")
print(f"Результат деления в true_math: {result2}")
print(f"Результат деления в true_math: {result3}")
print(f"Результат деления в true_math: {result4}")