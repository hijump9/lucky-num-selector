import random

def get_lucky_nums():
    return random.sample(range(1,45+1), k=6)


if __name__ == '__main__':
    print(get_lucky_nums())
