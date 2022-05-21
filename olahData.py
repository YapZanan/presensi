import face_recognition
import numpy as np
import os


class olahData():

    def buatEncoding(self, path_from):
        image = face_recognition.load_image_file(path_from)
        image_encoding = face_recognition.face_encodings(image)[0]
        return image_encoding

    def simpanEncoding(self, namaFile, encoding):
        with open(f"Encoding/{namaFile}.npy", 'wb') as f:
            np.save(f, encoding)

    def loadEncoding(self, namaFile):
        with open('Encoding\\' + namaFile, 'rb') as f:
            encodingAmbil = np.load(f)
            return encodingAmbil
