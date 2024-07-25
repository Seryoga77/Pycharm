calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    calls += 1
    chameleon_down = string.lower()
    chameleon_up = string.upper()
    this_is_the_length = len(string)
    return this_is_the_length, chameleon_up, chameleon_down


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)