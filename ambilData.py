import shutil

import cv2
import numpy as np
import datetime
import os
import csv
import pandas as pd
import os
import olahData
class ambilData():
    def __init__(self):

        self.direktori = 'Belajar'
        self.direktori_sudah = 'Sudah_Belajar'
        self.NIM, self.nama = self.baca()
        self.path = os.listdir(self.direktori)
        self.olahData = olahData.olahData()
        self.ambil()

        # print(self.NIM)
        # print(self.nama)

        # print(self.olahData.loadEncoding("5191011008_Maya_Listiyani.npy"))

    def ambil(self):
        for kelas in self.path:
            loadData = cv2.imread(f'{self.direktori}/{kelas}')

            data = self.convert(self.NIM, self.nama)
            self.masukKeCSV(data)

            nama = self.ambilNama(kelas)
            encod = self.olahData.buatEncoding(f'{self.direktori}/{kelas}')
            self.olahData.simpanEncoding(nama, encod)

            self.pindahData((self.direktori + "\\" + kelas), (self.direktori_sudah + "\\" + nama))

    def ambilNama(self, total):
        namaTanpaEkstensi = os.path.splitext(total)[0]
        array = namaTanpaEkstensi.split('_')
        folder_ = ' '.join(array)
        NIM = array.pop(0)
        nama = '_'.join(array)
        # self.nama.append(namaa)
        self.NIM.append(NIM)
        self.nama.append(nama)
        print((self.direktori + "/" + total))
        return namaTanpaEkstensi


    def convert(self, l1, l2):
        convert = [list(l) for l in zip(l1, l2)]
        # print(convert)
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
        # print(NIM)
        # print(nama)
        return NIM, nama


    def pindahData(self, path_from, path_to):
        isExist = os.path.exists(path_to)
        if not isExist:
            os.makedirs(path_to)
        shutil.move(path_from, path_to)


ambilData()