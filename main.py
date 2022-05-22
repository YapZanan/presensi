import time
from statistics import mean
import sys
from PyQt5 import QtWidgets, uic, QtGui

now = time.time()
import face_recognition
import numpy as np
import cv2

from imutils.video import WebcamVideoStream, FPS
import imutils

import olahData


class jalankan():
    def __init__(self):
        super(jalankan, self).__init__()
        # uic.loadUi('untitled.ui', self)
        self.olah = olahData.olahData()
        self.known_face_encodings = self.olah.encoding
        self.known_face_names = self.olah.nama
        self.webcamMulti()


    def webcamMulti(self):
        vs = WebcamVideoStream(src=0).start()
        fps = FPS().start()
        avg = []
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        while True:
            sekarang = time.time()
            frame = vs.read()
            small_frame = imutils.resize(frame, 480)

            rgb_small_frame = small_frame[:, :, ::-1]


            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                # top *= 4
                # right *= 4
                # bottom *= 4
                # left *= 4

                # Draw a box around the face
                cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(small_frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(small_frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


            cv2.imshow("Frame", small_frame)

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

    def webcam(self):
        fps = FPS().start()
        avg = []
        delay = []
        se = time.time()
        print("Time to start", se-now)
        video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        while True:
            sekarang = time.time()
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                # top *= 4
                # right *= 4
                # bottom *= 4
                # left *= 4

                # Draw a box around the face
                cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(small_frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(small_frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                # print(name)
                nanti = time.time()
                print("Delay: ", nanti - sekarang)
                avg.append(nanti - sekarang)
                average = (mean(avg))
                fps.update()

            # Display the resulting image
            cv2.imshow('Video', small_frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print(average)
                fps.stop()
                print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
                print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

# app = QtWidgets.QApplication(sys.argv)
# window = jalankan()
# window.show()
# app.exec_()

jalankan()