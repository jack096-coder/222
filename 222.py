import streamlit as st

# 設定網頁標題
st.title("🔢 總和計算機 (1 到 N)")

# 讓使用者輸入 N
n_value = st.number_input("請輸入一個整數 N：", min_value=1, value=10, step=1)

# 計算邏輯：使用公式 (1+N)*N / 2 效率最高
# 或是使用 sum(range(1, n_value + 1))
result = sum(range(1, n_value + 1))

# 顯示結果
st.subheader(f"計算結果：")
st.write(f"從 1 加到 {n_value} 的總和是：**{result}**")

# 額外的小裝飾：顯示計算過程
if n_value <= 20:
    process = " + ".join(str(i) for i in range(1, n_value + 1))
    st.text(f"計算過程: {process} = {result}")
else:
    st.info("當 N 較大時，僅顯示最終結果。")
