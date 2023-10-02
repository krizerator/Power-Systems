import numpy as np
import math

V1 = 1
theta1 = 0
P1 = []
Q1 = []
Z = complex(0, 0.1)
P2 = [-0.5]
Q2 = [-0.5]
theta2 = [0]
V2 = [1]

J = [
      [10*V2[0]*math.cos(theta2[0]), 10*math.sin(theta2[0])],
      [10*V2[0]*math.sin(theta2[0]), 20*V2[0]-10*math.cos(theta2[0])]
    ]

C = np.linalg.inv(J)
print(J)
print(C)

delta_theta2 = -C*[P2[0], Q2[0]]
print(delta_theta2)

# print(J[0][0])
# for i in range(len())

# Chrome, VSCode