import shutil

import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv
import pandas as pd
import os

class ambilData():
    def __init__(self):

        self.direktori = 'Belajar'
        self.direktori_sudah = 'Sudah_Belajar'
        self.NIM, self.nama = self.baca()
        self.path = os.listdir(self.direktori)
        self.ambil()

        print(self.NIM)
        print(self.nama)

    def ambil(self):
        for kelas in self.path:
            loadData = cv2.imread(f'{self.direktori}/{kelas}')
            self.ambilNama(kelas)



    def ambilNama(self, total):
        namaTanpaEkstensi = os.path.splitext(total)[0]
        array = namaTanpaEkstensi.split('_')
        folder_ = ' '.join(array)
        NIM = array.pop(0)
        nama = '_'.join(array)
        # self.nama.append(namaa)
        self.NIM.append(NIM)
        self.nama.append(nama)
        path = "Data\\NIMNama.csv"
        data = self.convert(self.NIM, self.nama)
        self.masukKeCSV(data)
        self.pindahData((self.direktori + "\\" + total), (self.direktori_sudah + "\\" + namaTanpaEkstensi))

    def convert(self, l1, l2):
        convert = [list(l) for l in zip(l1, l2)]
        print(convert)
        return convert

    def masukKeCSV(self, data):
        path = "Data\\NIMNama.csv"
        header = ["NIM", "Nama"]
        with open(path, "w") as outfile:
            write = csv.writer(outfile)
            write.writerow(header)
            write.writerows(data)

    def baca(self):
        NIM = []
        nama = []
        path = "Data\\NIMNama.csv"
        with open(path, "r+") as infile:
            data = csv.DictReader(infile)
            for col in data:
                NIM.append(col['NIM'])
                nama.append(col['Nama'])
        print(NIM)
        print(nama)
        return NIM, nama

    def pindahData(self, path_from, path_to):
        isExist = os.path.exists(path_to)
        if not isExist:
            os.makedirs(path_to)
        shutil.move(path_from, path_to)

    def simpanEncoding(self, path_to):
        print("aaa")

        with open('Encopding\\'+ path_to+'.npy', 'wb') as f:
            np.save(f, image_encoding)

ambilData()




# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.png")
image_encoding = face_recognition.face_encodings(image)[0]
# video_capture = cv2.VideoCapture(0)
# with open('test.npy', 'rb') as f:
#     a = np.load(f)

# known_face_encodings = [
#     # a
#     image_encoding
# ]
# #
# known_face_names = [
#     "Biden"
# ]

# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True

# end_times = time.time()
# print(end_times-start_time)
# while True:
#     # Grab a single frame of video
#     ret, frame = video_capture.read()
#
#
#     # Resize frame of video to 1/4 size for faster face recognition processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#
#     # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#     rgb_small_frame = small_frame[:, :, ::-1]
#
#     # Only process every other frame of video to save time
#     if process_this_frame:
#         # Find all the faces and face encodings in the current frame of video
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#
#         face_names = []
#         for face_encoding in face_encodings:
#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"
#
#             # # If a match was found in known_face_encodings, just use the first one.
#             # if True in matches:
#             #     first_match_index = matches.index(True)
#             #     name = known_face_names[first_match_index]
#
#             # Or instead, use the known face with the smallest distance to the new face
#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#
#             face_names.append(name)
#
#     process_this_frame = not process_this_frame
#
#
#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#         top *= 2
#         right *= 2
#         bottom *= 2
#         left *= 2
#
#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#         # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#     # Display the resulting image
#     cv2.imshow('Video', frame)
#
#     # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()

#
# print(image_encoding)
# print(type(image))
# print(type(image_encoding))
# print(len(image_encoding))
#
# with open('Belajar/adasd.npy', 'wb') as f:
#     np.save(f, image_encoding)
#
# with open('test.npy', 'rb') as f:
#     a = np.load(f)
#
# print(a)
#
# print(np.array_equal(image_encoding, a))

# pd.DataFrame(image_encoding).to_csv("aa.csv")

# aa = pd.DataFrame(image_encoding)
# aa.to_csv("aa.csv", header=False)
#
# print(image_encoding)
# print(type(image))
# print(type(image_encoding))
# print(len(image_encoding))
#
#
#
# df = read_csv("aa.csv", delimiter=",")
# print(df.values)