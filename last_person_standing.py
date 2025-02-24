def josephus(n, k=3):
    """
    模擬約瑟夫問題
    """
    people = list(range(1, n + 1))  # 初始化人員列表
    index = 0  # 報數起始索引

    while len(people) > 1:
        index = (index + (k - 1)) % len(people)  # 移動到報數 k 的人
        people.pop(index)  # 移除該人

    return people[0]  # 返回最後留下的人的順位

# 讓使用者輸入人數，確保輸入為有效數值
while True:
    try:
        n = int(input("請輸入總人數 (最多100): "))
        if 1 <= n <= 100:
            break
        else:
            print("人數必須介於 1 到 100 之間，請重新輸入。")
    except ValueError:
        print("請輸入有效的整數值！")

# 顯示最後留下的人的順位
last_person = josephus(n)
print("最後留下的同事是第", last_person, "順位")
