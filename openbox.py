def box_calu(box):
    sum = 0
    box1 = 1600
    box2to4 = 2400
    box4to44 = 2000
    box44toEX = 6000

    for i in range(box):
        if i == 0:
            sum += box1
        elif i > 0 and i < 4:
            sum += box2to4
        elif i >= 4 and i < 44:
            sum += box4to44
        elif i >= 44:
            sum += box44toEX
    return sum

def main():
    print('現在の箱数を入力してください。')
    box = int(input())
    now_coins = box_calu(box)
    print('目標箱数を入力してください。')
    goal = int(input())
    goal_coins = box_calu(goal)
    need_coins = goal_coins - now_coins
    print('あなたがあと必要とする戦貨は、' + str(need_coins) + '枚です。')
    print('今持っている戦貨は？')
    have_coins = int(input())
    print('個人ランキングの戦貨数は？')
    rank_coins = int(input())
    must_coins = need_coins - have_coins
    must_coins = must_coins - rank_coins
    print('あなたは、あと' + str(must_coins) + '枚稼がなければなりません。')

if __name__ == "__main__":
    main()