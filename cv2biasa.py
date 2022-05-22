import time
from statistics import mean

import cv2
import imutils
from imutils.video import FPS

vid = cv2.VideoCapture(0)
avg =[]
fps = FPS().start()
while True:
    sekarang = time.time()
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # Display the resulting frame
    frame = imutils.resize(frame, 400)
    cv2.imshow('frame', frame)
    nanti = time.time()
    print("Delay: ", nanti - sekarang)
    avg.append(nanti-sekarang)
    average = (mean(avg))
    fps.update()

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(average)
        fps.stop()
        print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()