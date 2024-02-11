import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_sphere(radius, center=(0, 0, 0), num_points=30):
    """Create a sphere in 3D space."""
    phi, theta = np.mgrid[0.0:np.pi:num_points*1j, 0.0:2.0*np.pi:num_points*1j]
    x = radius * np.sin(phi) * np.cos(theta) + center[0]
    y = radius * np.sin(phi) * np.sin(theta) + center[1]
    z = radius * np.cos(phi) + center[2]
    return x, y, z

# Define the radius of the sphere
radius = 1.0

# Create points on the surface of the sphere
x, y, z = create_sphere(radius)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere
ax.scatter(x, y, z, s=1, label='Sphere Points')

# Add the center point (0, 0, 0)
ax.scatter([0], [0], [0], color='red', marker='o', label='Center (0, 0, 0)')

# Draw lines dividing octants
ax.plot([0, 0], [0, 0], [-radius, radius], color='black', linestyle='--')  # x-axis
ax.plot([0, 0], [-radius, radius], [0, 0], color='black', linestyle='--')  # y-axis
ax.plot([-radius, radius], [0, 0], [0, 0], color='black', linestyle='--')  # z-axis

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Sphere with Octant Divisions')

# Show legend


plt.show()
