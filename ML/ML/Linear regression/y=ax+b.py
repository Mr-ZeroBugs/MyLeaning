import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
y = 2*x+1

plt.plot(x, y, "r", label="y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Graph")
plt.grid()
plt.show()
#มันขึ้นไปอย่างคงที่ เนื่องจาก a เเละ b ที่กำหนดขึ้นมา เป้นค่าคงตัว คือ2 เเละ 1 ต่อไปจะมาลอง random gพื่อให้เกิดการกระจาย ต่อใน distribution.py
