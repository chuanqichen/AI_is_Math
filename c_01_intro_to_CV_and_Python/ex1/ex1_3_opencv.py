# %% [markdown]
# # EX 1.3- Opencv: forest pyramid
# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_01_intro_to_CV_and_Python/ex1/forest.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_01_intro_to_CV_and_Python/ex1/pyramids.png'.split())
    
# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2
# %%

forest_img = cv2.imread("forest.jpg")
pyramid_img = cv2.imread("pyramids.png")
forest_img = cv2.cvtColor(forest_img,cv2.COLOR_BGR2GRAY)
pyramid_img = cv2.cvtColor(pyramid_img,cv2.COLOR_BGR2GRAY)


# %%
# TODO: your goal is to build the pyramids in the forest!
#  Hints to think about:
#  - are the images the same size?
#  - How to mask/overlay the pixels from pyramids image to forest image (use numpy masks that we've seen in the numpy notebook!!!)
#
#  TODO: this section can be done in 3-5 lines of nice looking code, try not to write more then 10 lines here.
res_im = np.zeros_like(forest_img)
pyramid = pyramid_img[0:460, :]
res_im[0:pyramid.shape[0], 0:pyramid.shape[1]] = pyramid
mask = res_im==0
res_im[mask]=forest_img[mask]
#res_im[res_im>160]=forest_img[res_im>160]
# %%
plt.figure()
plt.imshow(res_im, cmap='gray', vmin=0, vmax=255)
plt.show()
# %%
