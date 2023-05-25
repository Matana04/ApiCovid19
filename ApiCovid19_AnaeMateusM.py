from PyQt5 import  uic
import PyQt5.QtWidgets as QtWidgets

import sys
import requests
import json
import pandas as pd
class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('C:/Users/mateu/Desktop/ApiCovid19/tela_api.ui', self)
        self.show()

        vetor = ["ac", "al", "ap", "am", "ba", "ce", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi", "rj", "rn", "ro", "rs", "rr", "sc", "sp", "se", "to", "df"]

        self.comboBox.addItems(vetor)
        self.consultaButton.clicked.connect(self.opc)
        self.consultaButton_2.clicked.connect(self.pegatxt)

    def opc(self):
        inputUF = self.comboBox.currentText()

        reqURL = f'https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{inputUF}'
        print(reqURL)

        response = requests.get(reqURL)

        contentJson = json.loads(response.content)


        if contentJson != {"error": "state not found"}:

            uid = contentJson["uid"]
            uf = contentJson["uf"]
            estado = contentJson["state"]
            casos = contentJson["cases"]
            obitos = contentJson["deaths"]
            suspeitos = contentJson["suspects"]
            recusados = contentJson["refuses"]
            data = contentJson["datetime"]

            resultApi = f'UID: {uid}\n'
            resultApi += f'UF: {uf}\n'
            resultApi += f'Estado: {estado}\n'
            resultApi += f'Casos: {casos}\n'
            resultApi += f'Obitos: {obitos}\n'
            resultApi += f'Suspeitos: {suspeitos}\n'
            resultApi += f'Casos Recusados: {recusados}\n'
            resultApi += f'Data: {data}'

            self.textBrowser.setText(resultApi)

        else:
            self.textBrowser.setText("UF não reconhecida.")

    def pegatxt(self):
        inputtxt = self.textEdit.toPlainText()

        dadoscovid19 = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/{inputtxt}')
        dicCovid = json.loads(dadoscovid19.content)

        dicCovid2 = dicCovid['data']

        Estados = []
        Casos = []
        Mortes = []

        for state in dicCovid2:
            listEstados = state
            listEstados2 = listEstados.values()
            listEstados2 = list(listEstados2)
            Estados.append(listEstados2[2])
            Casos.append(listEstados2[3])
            Mortes.append(listEstados2[4])

        tabela = pd.DataFrame(columns=["Estados", "Casos", "Mortes"],
                              data=zip(Estados, Casos, Mortes))

        self.textBrowser_2.setText(tabela.__str__())

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()