calls = 0

def count_calls():
    global calls
    calls = calls + 1
#
def string_info(string):
    to_change = len(string), string.upper(), string.lower()
    to_change = tuple(to_change)
    print(to_change)
    count_calls()

string_info(input('Введите строку: '))
string_info('peppermint candy cane')


def is_contains(string, list_to_search):
    if string.upper() in str(list_to_search).upper():
        print(True)
    else:
        print(False)

    count_calls()

is_contains('Peach', ['peach', 'pear', 'pomegranate'])
is_contains('rice', ['wine', 'garlic', 'onion', 'parmesan', 'bullion', 'riCe'])

print(calls)