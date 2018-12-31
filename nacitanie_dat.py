import glob
import os
import numpy as np
import pandas as pd
from datetime import datetime


class Nacitanie_dat:
    def __init__(self, vlnova_dlzka):
        self.txt_subory = os.getcwd() + "\\*.txt"
        self.vlnova_dlzka = vlnova_dlzka

    def nacitanie_txt_suborov(self):
        txt_subory = []
        for file in glob.glob(self.txt_subory):
            txt_subory.append(file)
        return txt_subory

    # def zoradenie_podla_datumu(self):
    #     zoznam_datumov = list()
    #     for kazdy_datum in self.nacitanie_txt_suborov():
    #         datum_parser = kazdy_datum[-17:-7]
    #         datum = datetime.strptime(datum_parser, '%Y-%m-%d')
    #         zoznam_datumov.append(datum + kazdy_datum[-1:-6])
    #     return zoznam_datumov

    def ocistenie_txt_suborov(self):
        data_list = list()
        for data_file in self.nacitanie_txt_suborov():
            data = pd.read_table(data_file, sep='\t', skiprows=2, decimal=',', usecols=[6, 7])
            data_list.append(data)

        return data_list

    def vybratie_spravnej_vlnovej_dlzky(self):
        zoznam_dat_so_spravnymi_vlnovymi_dlzkami = list()
        for i in self.ocistenie_txt_suborov():
            s = i[i.Wavelength == self.vlnova_dlzka]
            zoznam_dat_so_spravnymi_vlnovymi_dlzkami.append(s)

        return zoznam_dat_so_spravnymi_vlnovymi_dlzkami

    def rozdelenie_data_frejmov_na_mensie_celky(self):
        viacere_rozdelene_data_frejmy = list()

        for i in self.vybratie_spravnej_vlnovej_dlzky():
            rozdeleny_data_frejm = [i['Abs'][j:j + 6] for j in range(0, len(i['Abs']), 6)]
            viacere_rozdelene_data_frejmy.append(rozdeleny_data_frejm)

        return viacere_rozdelene_data_frejmy

    def vlozenie_parcialnych_data_frejmov_do_slovnikov(self):
        nazvy = list()
        nazvy_suborov = [x for x in self.nacitanie_txt_suborov()]
        for j in nazvy_suborov:
            # nazov = j[-17] + j[-16] + j[-15] + j[-14] + j[-13] + j[-12] + j[-11] + j[-10] + j[-9] + j[-8] + j[-7] + j[-6] + j[-5]
            nazov = j[-17:-4]
            nazvy.append(nazov)

        slovnik_s_datami = dict()
        pocitadlo = 0

        for i in nazvy:
            slovnik_s_datami[i] = self.rozdelenie_data_frejmov_na_mensie_celky()[pocitadlo]
            pocitadlo += 1
        return slovnik_s_datami








a = Nacitanie_dat(682)
# print(a.rozdelenie_data_frejmov_na_mensie_celky())
# print(a.priemer())
print(a.vlozenie_parcialnych_data_frejmov_do_slovnikov())
# print(a.nacitanie_txt_suborov())
