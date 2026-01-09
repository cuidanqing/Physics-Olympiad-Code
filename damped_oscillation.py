import numpy as np
import matplotlib.pyplot as plt

# 1. 设置中文字体 / Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 2. 定义物理参数 / Define Physical Parameters
m = 1.0       # 质量 (kg)
k = 25.0      # 劲度系数 (N/m)
b = 1.0       # 阻尼系数 (N s/m) -> 试着把这个改成 10 看看会发生什么？
A = 10.0      # 初始振幅 (m)

# 3. 计算中间变量 (竞赛核心逻辑) / Calculate Intermediate Variables
# 固有角频率 (Natural Angular Frequency)
omega_0 = np.sqrt(k / m)

# 衰减系数 (Damping Ratio)
gamma = b / (2 * m)

# 阻尼振动角频率 (Damped Angular Frequency)
# 必须保证 omega_0 > gamma (欠阻尼 Under-damped)，否则就不振动了
omega_prime = np.sqrt(omega_0**2 - gamma**2)

# 时间轴
t = np.linspace(0, 10, 500)

# 4. 核心公式 / Core Formulas
# 位移方程 / Displacement Equation
x = A * np.exp(-gamma * t) * np.cos(omega_prime * t)

# 包络线 (振幅限制) / Envelope Lines (Amplitude Limit)
envelope_upper = A * np.exp(-gamma * t)
envelope_lower = -A * np.exp(-gamma * t)

# 5. 绘图 / Plotting
plt.figure(figsize=(10, 6))

# 画包络线 (虚线) / Plot Envelopes (Dashed lines)
plt.plot(t, envelope_upper, 'r--', linewidth=1.5, label=r'包络线 $\pm Ae^{-\gamma t}$')
plt.plot(t, envelope_lower, 'r--', linewidth=1.5)

# 画实际振动 (实线) / Plot Actual Oscillation (Solid line)
plt.plot(t, x, 'b-', linewidth=2, label=r'位移 $x(t)$')

# 装饰图表 / Decoration
plt.title(f'阻尼振动 (Damped Oscillation)\n$b={b}, k={k}, m={m}$', fontsize=16)
plt.xlabel('时间 t (s)', fontsize=14)
plt.ylabel('位移 x (m)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12, loc='upper right')

# 6. 保存并显示 / Save and Show
filename = 'damped_oscillation.png'
plt.savefig(filename, dpi=300)
print(f"图像已保存为 {filename}")
plt.show()