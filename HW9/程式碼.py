def print_matrix(s1, s2, dp):
    """
    這是一個輔助函式，用來漂亮地印出矩陣
    """
    print("\n--- 編輯距離計算矩陣 ---")
    # 印出頂部標題 (s2)
    header = "      " + "  ".join(s2)
    print(header)
    
    for i, row in enumerate(dp):
        # 處理每一行的開頭字母 (s1)
        row_label = s1[i-1] if i > 0 else " "
        # 格式化數字，確保對齊
        formatted_row = "  ".join(f"{num:1d}" for num in row)
        print(f"{row_label} {formatted_row}")
    print("-" * 25)

def calculate_edit_distance():
    # 讓使用者輸入文字
    word1 = input("請輸入第一個字串 (s1): ").strip()
    word2 = input("請輸入第二個字串 (s2): ").strip()

    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j

    # 動態規劃計算
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # 刪除
                                   dp[i][j-1],    # 插入
                                   dp[i-1][j-1])  # 替換

    # 印出視覺化結果
    print_matrix(word1, word2, dp)
    print(f"『{word1}』 轉換為 『{word2}』 的最小編輯距離是: {dp[m][n]}")

# 執行程式
if __name__ == "__main__":
    calculate_edit_distance()
