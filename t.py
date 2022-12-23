from skimage import data, io, filters

image = data.coins()
print(f"{image=}")
print(f"{len(image)=}")
# ... or any other NumPy array!
edges = filters.sobel(image)
io.imshow(edges)
io.show()