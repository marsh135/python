import numpy as np

import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, len(x))
y2 = np.cos(x) + np.random.normal(0, 0.1, len(x))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Noisy Sine Wave', color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label='Noisy Cosine Wave', color='green', linestyle='-', marker='x')

# Add titles and labels
plt.title('Visualization of Noisy Sine and Cosine Waves', fontsize=16)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)

# Add grid and legend
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()