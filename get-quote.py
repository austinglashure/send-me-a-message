import random

quotes = open("quotes.txt", 'r')
quotes_list = quotes.readlines()

def get_valid_random_line():
    running = True
    while running:
        foo = random.randint(0, len(quotes_list))
        if foo % 2 == 0:
            running = False
    return foo

num = get_valid_random_line()
print(quotes_list[num], quotes_list[num + 1])

quotes.close()
print("done")
