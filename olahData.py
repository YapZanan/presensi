import face_recognition
import numpy as np
import os



class olahData():
    def __init__(self):
        self.NPY = 'Encoding'
        self.pathNPY = os.listdir(self.NPY)
        self.encoding = []
        self.NIM = []
        self.nama = []
        self.ambilSemua()

        print(self.NIM)
        print(self.nama)
        print(self.encoding)

    def ambilSemua(self):
        for kelas in self.pathNPY:
            NIM, nama = self.ambilNamaNPY(kelas)
            self.NIM.append(NIM)
            self.nama.append(nama)
            self.encoding.append(self.loadEncoding(kelas))


    def buatEncoding(self, path_from):
        image = face_recognition.load_image_file(path_from)
        image_encoding = face_recognition.face_encodings(image)[0]
        return image_encoding

    def simpanEncoding(self, namaFile, encoding):
        with open(f"Encoding/{namaFile}.npy", 'wb') as f:
            np.save(f, encoding)

    def loadEncoding(self, namaFile):
        with open('Encoding\\'+namaFile, 'rb') as f:
            encodingAmbil = np.load(f)
            return encodingAmbil

    def ambilNamaNPY(self, path_from):
        namaTanpaEkstensi = os.path.splitext(path_from)[0]
        array = namaTanpaEkstensi.split('_')
        folder_ = ' '.join(array)
        NIM = array.pop(0)
        nama = '_'.join(array)
        # self.nama.append(namaa)
        return NIM, nama

