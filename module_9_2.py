first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]

second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
