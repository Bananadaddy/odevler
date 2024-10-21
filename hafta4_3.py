#Rolling a dice
import random

frekans1 = frekans2 = frekans3 = frekans4 = frekans5 = frekans6 = 0

for zar_at in range(6_000_000):
    zar_yuzu = random.randrange(1,7)

    if zar_yuzu == 1:
        frekans1 += 1
    elif zar_yuzu == 2:
        frekans2 += 1
    elif zar_yuzu == 3:
        frekans3 += 1
    elif zar_yuzu == 4:
        frekans4 += 1
    elif zar_yuzu == 5:
        frekans5 += 1
    elif zar_yuzu == 6:
        frekans6 += 1