def generate_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return  result


for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - { result}")