import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def getPongState(im):
    im_scaled_green = im[:, :, 1] / np.mean(im, axis=2)
    grtop = im_scaled_green[35:190, 142]
    g_y = np.argmax(grtop)

    im_scaled_red = im[:, :, 0] / np.mean(im, axis=2)
    rtop = im_scaled_red[35:190, 18]
    # plt.imshow(rtop)
    # plt.show()
    # time.sleep(20)
    r_y = np.argmin(rtop)

    ball = im[35:190, :, :].mean(axis=2)
    bmx = np.argmax(ball)
    b_x, b_y = (bmx % im.shape[1], bmx / im.shape[1])

    return g_y, r_y, b_x, b_y