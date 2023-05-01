import random

# 주어진 숫자 리스트
numbers = list(range(1, 46))

while True:
    # 사용자가 원하는 만큼 반복 수행
    repeat = input("몇 번을 반복하시겠습니까? (숫자 입력): ")
    
    try:
        repeat = int(repeat)
        if repeat <= 0:
            print("0 이상의 숫자를 입력해주세요.")
            continue
        break
    except ValueError:
        print("숫자를 입력해주세요.")

for i in range(repeat):
    # 리스트에서 6개를 무작위로 선택
    selected = random.sample(numbers, 6)
    print(f"{i+1}번째 선택된 숫자: {selected}")
