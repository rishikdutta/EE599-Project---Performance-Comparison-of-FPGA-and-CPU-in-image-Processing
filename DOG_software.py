from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy import misc
%matplotlib inline
image_path = "sahara.jpg"
original_image = Image.open(image_path) 
df_image = Image.open(image_path)
f_image = Image.open(image_path)
canvas = plt.gcf()
size = canvas.get_size_inches()
canvas.set_size_inches(size*2)

old_width, old_height = original_image.size
print("Image size: {}x{} pixels.".format(old_width, old_height))
_ = plt.imshow(original_image)
ascent = misc.ascent()
f_result = gaussian_filter(original_image, sigma=5)canvas = plt.gcf()
size = canvas.get_size_inches()
canvas.set_size_inches(size*2)

old_width, old_height = original_image.size
print("Image size: {}x{} pixels.".format(old_width, old_height))
_ = plt.imshow(f_result)
df_result = gaussian_filter(f_result, sigma=5)
canvas = plt.gcf()
size = canvas.get_size_inches()
canvas.set_size_inches(size*2)

old_width, old_height = original_image.size
print("Image size: {}x{} pixels.".format(old_width, old_height))
_ = plt.imshow(df_result)
buffer1    = np.asarray(f_result);
buffer2    = np.asarray(df_result);
buffer3    = buffer1 - buffer2;
differenceImage = Image.fromarray(buffer3);
canvas = plt.gcf()
size = canvas.get_size_inches()
canvas.set_size_inches(size*2)

old_width, old_height = original_image.size
print("Image size: {}x{} pixels.".format(old_width, old_height))
_ = plt.imshow(differenceImage)
%%timeit
ffff_result = gaussian_filter(original_image, sigma=5)
dfff_result = gaussian_filter(ffff_result, sigma=5)
buffer1    = np.asarray(ffff_result);
buffer2    = np.asarray(dfff_result);
buffer3    = buffer1 - buffer2;
differenceImage = Image.fromarray(buffer3);