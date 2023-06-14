import cv2
import numpy as np


class ImgInput:
    '''
    This class is used to input image from camera or video file
    '''
    def init(self, path: str, img: np.ndarray) -> None:
        '''
        This function initializes the class

        Parameters
        ----------
        path : str
            path to the video file
        Returns
        -------
        None

        '''
        self.path = path
        self.img = img

    def get_img(self, path) -> np.ndarray:
        '''
        This function returns a frame from the video file
        Parameters
        ----------
        None

        Returns
        -------
        frame : numpy.ndarray
            frame from the video file

        '''
        self.img = cv2.imread(path, 0)  # read image in grayscale

        return self.img

    def cv_show(self, name: str, img: np.ndarray) -> None:
        '''
        This function shows image in a window

        Parameters
        ----------
        name : str
            name of the window
        img : numpy.ndarray
            image to be shown       
        Returns
        -------
        None

        '''

        cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)
        cv2.startWindowThread()
        cv2.imshow(name, img)  # show image

        # close window if q is pressed
        key = cv2.waitKey(0)
        if key in [27, ord('q'), ord('Q')]:
            cv2.destroyAllWindows()
        cv2.waitKey(1)  # this is necessary to close window ************