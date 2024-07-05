num = 0
player = 'playerA'

while num < 31:
    print(player)
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

    if num >= 31:
        if player == 'playerA':
            print("playerB	win!")
        else:
            print("playerA	win!")
        break
    
    if player == 'playerA':
        player = 'playerB'
    else:
        player = 'playerA'