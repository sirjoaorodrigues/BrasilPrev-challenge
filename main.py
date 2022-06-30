import random
import pandas as pd


def board():
    value = [random.randrange(1, 100, 1) for i in range(1, 21)]
    properties = list(range(1, 21))

    info = pd.DataFrame(value, properties)
    print(info)


def random_start():
    player = random.randint(1, 4)
    return player


random_start()
board()
