import cv2

#input video
vidcap = cv2.VideoCapture('./shahar_jack.avi')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:

        #write image frames
        cv2.imwrite("./image"+str(count)+".jpg", image)
    return hasFrames
sec = 0
frameRate = 0.17
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
