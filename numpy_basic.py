import numpy as np
from PIL import Image
arr = np.array([1,2,3,4,5,6])
resh = arr.reshape(2,3)
print(resh)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# print(arr2.shape)

# zeros = np.zeros((3,3))
# print(zeros)

# ones = np.ones((3,3))
# print(ones)

# id = np.eye(3,3)
# print(id)

# random = np.random.rand(3,3)
# print(random)

# a = np.array([1,2,3],[4,5,6])
# b = np.array([5,6,7],[8,9,10])
# print(np.dot(a,b))

# print(a[1:3])
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[:1,1:])
# print(a[2:,:1])
# print(a[1:,1:])

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1,2],[3,4],[5,6]])
# prod = np.dot(a,b)
# print(prod)

# resh = a.reshape(3,2)
# print(np.sum(a))
# print(np.min(a))
# print(np.sum(a))
# print(np.std(a))
# print(np.mean(a))

# img = Image.open("photo_jpg (1).jpg")
# img_arry = np.array(img)
# print(img_arry)
# gray = 0.2989*img_arry[:,:,0]+0.5870*img_arry[:,:,1]+0.1140*img_arry[:,:,2]
# gray_img = Image.fromarray(gray.astype('uint8'))
# gray_img.show()