import cv2
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

def region_grow(img, seeds, thresh):
    h, w = img.shape
    seg = np.zeros_like(img, dtype=np.uint8)
    visited = np.zeros_like(img, bool)
    q = deque(seeds)
    for y,x in seeds:
        seg[y,x] = 255
        visited[y,x] = True

    while q:
        y, x = q.popleft()
        for dy in (-1,0,1):
            for dx in (-1,0,1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny,nx]:
                    if abs(int(img[ny,nx]) - int(img[y,x])) <= thresh:
                        seg[ny,nx] = 255
                        visited[ny,nx] = True
                        q.append((ny,nx))
    return seg

# load noisy image
noisy = cv2.imread('../results/noisy.png', cv2.IMREAD_GRAYSCALE)

# define seed points inside circle and square
seeds = [(60,60), (150,150)]
thresh = 20

segmented = region_grow(noisy, seeds, thresh)
cv2.imwrite('../results/region_growing.png', segmented)

# visualize
plt.figure(figsize=(6,6))
plt.title('Region Growing')
plt.imshow(segmented, cmap='gray')
plt.axis('off')
plt.show()
