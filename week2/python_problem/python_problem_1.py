num = 0

while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if num in [1, 2, 3]:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")

for i in range(1, num + 1):
    print(f"playerA : {i}")


while True:
    try:
        call_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if call_count in [1, 2, 3]:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")

num += call_count
for i in range(1, call_count + 1):
    print(f"playerB : {num - call_count + i}")