import random

def get_lucky_nums():
    return random.sample(range(1,45+1), k=6)

if __name__ == '__main__':
    times = int(input('Enter num(1-100): '))
    for _ in range(times):
        print(get_lucky_nums())
