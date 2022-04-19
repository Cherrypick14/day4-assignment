import itertools as itt

def cycle_dta(item):
    return itt.cycle(item)

result = cycle_dta(['S','K','A','E','H','U','B'])

for i in result:
    print(i)