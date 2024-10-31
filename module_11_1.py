import requests

# Отправка GET-запроса
response = requests.get('https://api.github.com')

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

import numpy as np

# 1. Создание массива
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# 2. Выполнение математических операций
# Сложение
array_sum = array_1d + 10
print("Array after addition:", array_sum)

# Умножение
array_product = array_1d * 2
print("Array after multiplication:", array_product)

# 3. Использование статистических функций
mean_value = np.mean(array_1d)
print("Mean value of array:", mean_value)

std_deviation = np.std(array_1d)
print("Standard deviation of array:", std_deviation)

from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('example.jpg')

# Изменение размера
resized_image = image.resize((300, 300))
resized_image.save('resized_example.jpg')

# Применение фильтра
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('blurred_example.jpg')

