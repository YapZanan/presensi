import time
from statistics import mean

import cv2
from imutils.video import WebcamVideoStream, FPS
import imutils

print("aaa")
print("bbb")
avg =[]
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()
while True:
	sekarang = time.time()
	frame = vs.read()
	frame = imutils.resize(frame, 400)
	cv2.imshow("Frame", frame)
	nanti = time.time()
	print("Delay: ", nanti - sekarang)
	avg.append(nanti - sekarang)
	average = (mean(avg))
	fps.update()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print(average)
		fps.stop()
		print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
		print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
		break

# Release handle to the webcam
cv2.destroyAllWindows()
vs.stop()