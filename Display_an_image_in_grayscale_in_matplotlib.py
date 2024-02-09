# storing image path
fname = r'g4g.png'

# opening image using pil
image = image.open(fname).convert("L")

# mapping image to gray scale
plt.imshow(image, cmap='gray')
plt.show()
