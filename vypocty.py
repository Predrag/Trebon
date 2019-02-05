from nacitanie_dat import Nacitanie_dat
import pandas as pd
import operator
import numpy as np


class Statistika(Nacitanie_dat):

    def __init__(self, vlnova_dlzka):
        super().__init__(vlnova_dlzka)

    # def vypocet_priemeru(self):
    #     slovnik = dict()
    #     vrat_slovnik = dict()
    #     for key, value in self.vlozenie_parcialnych_data_frejmov_do_slovnikov().items():
    #         vrat_slovnik[key] = [pd.DataFrame.mean(value[s]) for s in range(0, len(value))]
    #         slovnik.update(vrat_slovnik)
    #     return slovnik

    def vypocet_priemeru(self):
        slovnik = dict()
        vrat_slovnik = dict()
        for key, value in self.vlozenie_parcialnych_data_frejmov_do_slovnikov().items():
            vrat_slovnik[key] = [pd.DataFrame.mean(value[s]) for s in range(0, len(value))]
            slovnik.update(vrat_slovnik)

        return slovnik

    # def vypocet_strednej_odchylky(self):
    #     slovnik = dict()
    #     vrat_slovnik = dict()
    #     for key, value in self.vlozenie_parcialnych_data_frejmov_do_slovnikov().items():
    #         vrat_slovnik[key] = [pd.DataFrame.std(value[s]) for s in range(0, len(value))]
    #         slovnik.update(vrat_slovnik)
    #     return slovnik

    def vypocet_strednej_odchylky(self):
        slovnik = dict()
        vrat_slovnik = dict()
        for key, value in self.vlozenie_parcialnych_data_frejmov_do_slovnikov().items():
            vrat_slovnik[key] = [pd.DataFrame.std(value[s]) for s in range(0, len(value))]
            slovnik.update(vrat_slovnik)
        return slovnik

    # def vypocet_K_crit(self):
    #     vrat_slovnik = dict()
    #     vlozenie = self.vlozenie_parcialnych_data_frejmov_do_slovnikov()
    #     for key, value in vlozenie.items():
    #             # vlozenie[key] = value[0]
    #             vlozenie[key] = [abs(value[j] - self.vypocet_priemeru()[0][j]) / self.vypocet_strednej_odchylky()[0][j] for j in range(len(value))]
    #             vrat_slovnik.update(vlozenie)
    #     return vrat_slovnik

    def vypocet_K_crit(self):
        vrat_slovnik = dict()
        vrat_slovnik2 = dict()
        f = list()
        vlozenie = self.vlozenie_parcialnych_data_frejmov_do_slovnikov()
        j = 0
        # v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for key, value in vlozenie.items():
            vlozenie[key] = [
                abs((value[j] - self.vypocet_priemeru()[key][j]) / self.vypocet_strednej_odchylky()[key][j]) for j in
                range(0, len(value))]
            # vrat_slovnik.update(vlozenie)
            f.append(vlozenie[key])

        pocitadlo = 0
        g = list()
        z = list()
        for key, value in vlozenie.items():
            for i in f:
                for j in i:
                    s = j.where(lambda x: x > 1.996,
                                lambda x: self.vlozenie_parcialnych_data_frejmov_do_slovnikov()[key][pocitadlo][::])
                    pocitadlo += 1
                    g = s.mask(s > 1.996)
                    z.append(g)
                pocitadlo = 0
        return z

        # for key, value in vlozenie.items():
        #     vrat_slovnik[key] = z





b = Statistika(750)
# print(b.vypocet_priemeru())
# print(b.vypocet_strednej_odchylky())
print(b.vypocet_K_crit())
