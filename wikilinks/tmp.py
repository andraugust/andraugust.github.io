import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


im = Image.open('/Users/andrew/Desktop/Doug/graph.png')

im = np.array(im)
plt.imshow(im)
plt.gca().axis('off')
plt.show()