import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definindo dois vetores 3D
A = np.array([1, 0, 0])
B = np.array([0, 1, 0])

# Produto vetorial (A × B)
C = np.cross(A, B)

print(f"Vetor A: {A}")
print(f"Vetor B: {B}")
print(f"Produto vetorial A x B: {C}")

# Gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origem comum
origin = np.zeros(3)

# Plotando os vetores A, B e C
ax.quiver(*origin, *A, color='r', label='A', arrow_length_ratio=0.1)
ax.quiver(*origin, *B, color='b', label='B', arrow_length_ratio=0.1)
ax.quiver(*origin, *C, color='g', label='A x B (produto vetorial)', arrow_length_ratio=0.1)

# Configurações do gráfico
ax.set_xlim([0, max(A[0], B[0], C[0], 1)])
ax.set_ylim([0, max(A[1], B[1], C[1], 1)])
ax.set_zlim([0, max(A[2], B[2], C[2], 1)])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Produto Vetorial de Vetores 3D')
ax.legend()

plt.show()
