import random

# じゃんけんの手を表すリスト
hands = ["グー", "チョキ", "パー"]

def judge_winner(a_hand, b_hand):
    # 勝敗判定
    if a_hand == b_hand:
        return "draw"
    elif (a_hand == 0 and b_hand == 1) or (a_hand == 1 and b_hand == 2) or (a_hand == 2 and b_hand == 0):
        return "A"
    else:
        return "B"

def simulate_janken():
    # それぞれの勝ち数を格納
    a_wins = 0
    b_wins = 0
    draws = 0
    
    for i in range(3): #3回勝負
        
        # AとBの手をランダムに選ぶ
        a_hand = random.randint(0, 2)
        b_hand = random.randint(0, 2)
        
        # 勝敗を判定
        result = judge_winner(a_hand, b_hand)
        
        if result == "A":
            a_wins += 1
            print(f"第{i+1}戦: Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → Aの勝ち")
        elif result == "B":
            b_wins += 1
            print(f"第{i+1}戦: Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → Bの勝ち")
        else:
            draws += 1
            print(f"第{i+1}戦: Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → 引き分け！")
        
# 最終的な勝敗を表示
    print("\n最終結果:")
    print(f"Aの勝ち数: {a_wins}")
    print(f"Bの勝ち数: {b_wins}")
    print(f"引き分け数: {draws}") 
    
    if a_wins > b_wins:
        print("Aの勝ち")
    elif b_wins > a_wins:
        print("Bの勝ち")
    else: 
        print("引き分け！")

"""結果を表示
    print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")
"""
# じゃんけんのシミュレーションを実行
simulate_janken()

