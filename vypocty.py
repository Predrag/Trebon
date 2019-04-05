from nacitanie_dat import Nacitanie_dat
import pandas as pd
import matplotlib.pyplot as plt


class Statistika(Nacitanie_dat):

    def __init__(self, vlnova_dlzka):
        super().__init__(vlnova_dlzka)

    def vypocet_priemeru(self):
        priemer_zoznam = list()
        rozdeleny_priemer_zoznam = list()
        velkost_zoznamu = len(self.rozdelenie_data_frejmov_na_mensie_celky())

        for j in range(0, velkost_zoznamu):
            for i in self.rozdelenie_data_frejmov_na_mensie_celky()[j]:
                df = pd.DataFrame(i)
                ds = df['Abs'].mean()
                priemer_zoznam.append(ds)

            n = len(self.rozdelenie_data_frejmov_na_mensie_celky()[0])
            rozdeleny_priemer_zoznam = [priemer_zoznam[i * n:(i + 1) * n] for i in
                                        range((len(priemer_zoznam) + n - 1) // n)]

        return rozdeleny_priemer_zoznam

    def vypocet_strednej_odchylky(self):
        stredna_odchylka_zoznam = list()
        rozdelena_stredna_odchylka_zoznam = list()
        velkost_zoznamu = len(self.rozdelenie_data_frejmov_na_mensie_celky())

        for j in range(0, velkost_zoznamu):
            for i in self.rozdelenie_data_frejmov_na_mensie_celky()[j]:
                df = pd.DataFrame(i)
                ds = df['Abs'].std()
                stredna_odchylka_zoznam.append(ds)

            n = len(self.rozdelenie_data_frejmov_na_mensie_celky()[0])
            rozdelena_stredna_odchylka_zoznam = [stredna_odchylka_zoznam[i * n:(i + 1) * n] for i in
                                                 range((len(stredna_odchylka_zoznam) + n - 1) // n)]

        return rozdelena_stredna_odchylka_zoznam

    def k_kriticke(self):

        vysledne_k_po_podmienke = list()
        d = []
        p = self.vypocet_priemeru()
        s = self.vypocet_strednej_odchylky()

        for i in self.rozdelenie_data_frejmov_na_mensie_celky():
            d.append(i)

        for j in range(0, len(self.rozdelenie_data_frejmov_na_mensie_celky())):
            for k in range(0, len(self.rozdelenie_data_frejmov_na_mensie_celky()[0])):
                docasne_k = abs(d[j][k] - p[j][k]) / s[j][k]
                df = pd.DataFrame(docasne_k)
                ds = df.where((df['Abs'] > 1.996), d[j][k], axis=0)
                da = pd.DataFrame(ds)
                dc = da.where(ds['Abs'] < 1.996)

                dc['Cas'] = 2

                dc.plot(x='Cas', y='Abs')
                # plt.show()
                vysledne_k_po_podmienke.append(dc)

        return vysledne_k_po_podmienke


cas = [1, 2]

b = Statistika(750)
# print(b.vypocet_priemeru())
# print(b.vypocet_strednej_odchylky())
print(b.k_kriticke())
