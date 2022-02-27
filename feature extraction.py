import cv2
import numpy as np

#input video
vidcap = cv2.VideoCapture('./01.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sift = cv2.SIFT_create(nfeatures=20)
        keypoints = sift.detect(gray, None)
        img2 = cv2.drawKeypoints(gray, keypoints, None, (0, 0, 255))

        #write image frames
        cv2.imwrite("./walk"+str(count)+".jpg", gray)
    return hasFrames
sec = 0
frameRate = 0.17
count=285
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

