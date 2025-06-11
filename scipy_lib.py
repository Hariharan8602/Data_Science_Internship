from scipy.ndimage import gaussian_filter
import imageio.v3 as imageio
import matplotlib.pyplot as plt

image = imageio.imread('photo_jpg (1).jpg')

blurred = gaussian_filter(image,sigma=30)

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(blurred)
plt.title("Blurred")
plt.show()