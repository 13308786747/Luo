import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# 生成心形的参数方程
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# 使用 Streamlit 在网页中显示爱心图形
st.title("Heart Shape")
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color='red')

# 设置图形的外观
ax.set_aspect('equal')  # 保证坐标轴比例相同
ax.axis('off')  # 隐藏坐标轴

# 在 Streamlit 中显示图像
st.pyplot(fig)
