import numpy as np
import matplotlib.pyplot as plt

# 1. 设置中文字体 (防止乱码) / Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

# 2. 定义物理参数 / Define physical parameters
A = 10.0       # 振幅 (Amplitude)
omega = 2.0    # 角频率 (Angular Frequency)
T_period = 2 * np.pi / omega # 周期
t = np.linspace(0, 3 * T_period, 500) # 时间轴：画3个周期

# 3. 核心物理公式 (体现微积分关系) / Core Physics Formulas (Calculus relationships)
# 位移 x(t)
x = A * np.cos(omega * t)

# 速度 v(t) = dx/dt (链式法则: cos -> -sin * omega)
v = -A * omega * np.sin(omega * t)

# 加速度 a(t) = dv/dt (链式法则: -sin -> -cos * omega)
a = -A * (omega**2) * np.cos(omega * t)

# 4. 绘图 / Plotting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# 图1: 位移 / Displacement
ax1.plot(t, x, 'b-', label=r'$x(t) = A \cos(\omega t)$')
ax1.set_ylabel(r'位移 $x$ (m)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper right')
ax1.set_title('简谐运动的位移、速度与加速度 (SHM Kinematics)', fontsize=14)

# 图2: 速度 / Velocity
ax2.plot(t, v, 'r-', label=r'$v(t) = -A\omega \sin(\omega t)$')
ax2.set_ylabel(r'速度 $v$ (m/s)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

# 图3: 加速度 / Acceleration
ax3.plot(t, a, 'g-', label=r'$a(t) = -A\omega^2 \cos(\omega t)$')
ax3.set_ylabel(r'加速度 $a$ (m/s$^2$)', fontsize=12)
ax3.set_xlabel(r'时间 $t$ (s)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.6)
ax3.legend(loc='upper right')

# 5. 自动保存并显示 / Auto-save and show
plt.tight_layout()
plt.savefig('SHM_kinematics.png', dpi=300)
print("图像已保存为 SHM_kinematics.png")
plt.show()