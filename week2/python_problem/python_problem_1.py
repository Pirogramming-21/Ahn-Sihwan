def brGame():
    global num, player
    while True:
        try:
            call_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if call_count in [1, 2, 3]:
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")

    for i in range(num + 1, num + call_count + 1):
        print(f"{player} : {i}")

    num += call_count

    if player == 'playerA':
        player = 'playerB'
    else:
        player = 'playerA'
    
    if num >= 31:
        print(f"{player} win!")
        return True
    
num = 0
player = 'playerA'
while True:
    if brGame():
        break