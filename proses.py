import time
from statistics import mean
from threading import Thread

import face_recognition
import numpy as np
import cv2

from imutils.video import WebcamVideoStream, FPS
import imutils

import olahData

class proses:
    def __init__(self, src, known_face_encodings, known_face_names, name = "aaaa"):
        print("aa")
        self.rgb_small_frame = src
        self.name = name
        self.known_face_encodings = known_face_encodings
        self.known_face_names = known_face_names
        self.returnname = None

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.cariEncoding, name=self.name, args=())
        t.daemon = True
        t.start()
        return self, self.returnname

    def cariEncoding(self):
        face_locations = face_recognition.face_locations(self.rgb_small_frame)
        face_encodings = face_recognition.face_encodings(self.rgb_small_frame, face_locations)
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

            self.returnname = name
