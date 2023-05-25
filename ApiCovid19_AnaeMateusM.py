from PyQt5 import  uic
import PyQt5.QtWidgets as QtWidgets

import sys
import requests
import json

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('C:/Users/mateu/Desktop/ApiCovid19/tela_api.ui', self)
        self.show()

        vetor = ["ac", "al", "ap", "am", "ba", "ce", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi", "rj",
                 "rn", "ro", "rs", "rr", "sc", "sp", "se", "to", "df"]

        self.comboBox.addItems(vetor)
        self.consultaButton.clicked.connect(self.opc)

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

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()