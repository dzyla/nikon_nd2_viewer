from nd2reader import ND2Reader
import cv2
import numpy as np
import easygui


def open_nd2():
    nikon_nd2 = easygui.fileopenbox()

    def nothing(x):
        pass

    with ND2Reader(nikon_nd2) as images:

        nikon_file = images
        z, x, y = np.max(images.metadata['frames']), np.max(images.metadata['width']),np.max(images.metadata['height'])

        cv2.namedWindow('ImageStack')
        cv2.namedWindow('ImageStack', cv2.WINDOW_NORMAL)
        cv2.createTrackbar('Slice', 'ImageStack', 0, z, nothing)
        while (1):
            slice = cv2.getTrackbarPos('Slice', 'ImageStack')

            img = nikon_file[slice-1]
            if (np.max(img) - np.min(img)) != 0:
               img = (img - np.min(img)) / (np.max(img) - np.min(img))
            img = cv2.resize(img, (500, 500))
            cv2.imshow('ImageStack', img)
            cv2.namedWindow('ImageStack', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('ImageStack', 500, 500)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                quit(1)

if __name__ == "__main__":
    open_nd2()
