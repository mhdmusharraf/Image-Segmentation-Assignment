
import numpy as np
import cv2
from matplotlib import pyplot as plt

# create 200×200 image: background=0, circle=128, square=255
img = np.zeros((200,200), dtype=np.uint8)
cv2.circle(img, (60,60), 40, 128, -1)
cv2.rectangle(img, (120,120), (180,180), 255, -1)
cv2.imwrite('../data/synthetic.png', img)

# parameters
mean, sigma = 0, 25
gauss = np.random.normal(mean, sigma, img.shape).astype('float32')
noisy = cv2.add(img.astype('float32'), gauss)
noisy = np.clip(noisy, 0, 255).astype('uint8')
cv2.imwrite('../results/noisy.png', noisy)


# Otsu’s thresholding
_, th = cv2.threshold(noisy, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# save and visualize
cv2.imwrite('../results/otsu_result.png', th)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.title('Noisy'); plt.imshow(noisy, cmap='gray'); plt.axis('off')
plt.subplot(1,2,2); plt.title(f"Otsu (T={_:.0f})"); plt.imshow(th, cmap='gray'); plt.axis('off')
plt.tight_layout(); plt.show()

