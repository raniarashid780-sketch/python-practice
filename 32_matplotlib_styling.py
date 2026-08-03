"""Day 3: matplotlib styling — labels, legends, colors, limits, and aspect ratio."""
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = [3, 4]
y1 = [2, 3]
y2 = [2, 6]
ax.plot(x, y1, label="Revenue", color="pink")
ax.plot(x, y2, label="Cost", color="purple")
ax.set_xlabel("Period")
ax.set_ylabel("Amount")
ax.set_title("Period amount trend")
# I chose these limits so the plotted points fit comfortably in the view and still leave a bit of space around them.
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 8)
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.quiver(0, 0, 5, 6, angles="xy", scale_units="xy", scale=1, color="blue", label="Vector A (5,6)")
ax.quiver(0, 0, -2, 5, angles="xy", scale_units="xy", scale=1, color="red", label="Vector B (-2,5)")
ax.set_xlim(-7, 7)
ax.set_ylim(-1, 9)
ax.set_xlabel("Revenue")
ax.set_ylabel("Cost")
# Without this, the axes would not use the same scale, and the vectors would look stretched rather than keeping their true geometry.
ax.set_aspect("equal")
ax.legend()
ax.set_title("Vectors from origin")
plt.show()