import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.imiew = QLineEdit()
        self.nazwiskow = QLineEdit()
        regex = QRegularExpression("[a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]+")
        self.imiew.setValidator(QRegularExpressionValidator(regex))
        self.nazwiskow.setValidator(QRegularExpressionValidator(regex))

        self.peselw = QLineEdit()
        self.peselw.setMaxLength(11)
        pesel_regex = QRegularExpression("[0-9]{11}")
        self.peselw.setValidator(QRegularExpressionValidator(pesel_regex))

        self.kod_input1 = QLineEdit()
        self.kod_input1.setMaxLength(2)
        self.kod_input1.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{2}")))
        self.kod_input2 = QLineEdit()
        self.kod_input2.setMaxLength(3)
        self.kod_input2.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{3}")))

        self.chlop = QRadioButton("Mężczyzna")
        self.baba = QRadioButton("Kobieta")

        self.woj_input = QComboBox()
        wojewodztwa = ["Dolnośląskie", "Malopolski", "Lubelskie", "Mazowieckie", "Wielkopolskie", "Swietokrzyskie", "Opolskie", "Warminsko-mazurskie"]
        self.woj_input.addItems(wojewodztwa)

        self.zain1=QCheckBox("Gry")
        self.zain2=QCheckBox("Muzyka")

        self.wyczysc = QPushButton("Wyczyść")
        self.wyslj = QPushButton("Wyślij")

        layout.addWidget(QLabel("Podaj imię:"))
        layout.addWidget(self.imiew)
        layout.addWidget(QLabel("Podaj nazwisko:"))
        layout.addWidget(self.nazwiskow)
        layout.addWidget(QLabel("PESEL:"))
        layout.addWidget(self.peselw)

        layout.addWidget(QLabel("Kod pocztowy:"))
        kod_layout = QHBoxLayout()
        kod_layout.addWidget(self.kod_input1)
        kod_layout.addWidget(QLabel("-"))
        kod_layout.addWidget(self.kod_input2)
        layout.addLayout(kod_layout)

        layout.addWidget(QLabel("Płeć:"))
        plec_layout = QHBoxLayout()
        plec_layout.addWidget(self.chlop)
        plec_layout.addWidget(self.baba)
        layout.addLayout(plec_layout)

        layout.addWidget(QLabel("Województwo:"))
        layout.addWidget(self.woj_input)

        layout.addWidget(QLabel("Zainteresowania:"))
        layout.addWidget(self.zain1)
        layout.addWidget(self.zain2)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.wyczysc)
        btn_layout.addWidget(self.wyslj)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        self.wyczysc.clicked.connect(self.wyczyscwszystko)
        self.wyslj.clicked.connect(self.wyslij)

    def wyczyscwszystko(self):
        self.imiew.clear()
        self.nazwiskow.clear()
        self.peselw.clear()
        self.kod_input1.clear()
        self.kod_input2.clear()
        self.chlop.setChecked(False)
        self.baba.setChecked(False)
        self.woj_input.setCurrentIndex(0)
        self.zain1.setChecked(False)
        self.zain2.setChecked(False)

    def wyslij(self):
        imie = self.imiew.text()
        nazwisko = self.nazwiskow.text()
        pesel = self.peselw.text()
        kod_pocztowy = f"{self.kod_input1.text()}-{self.kod_input2.text()}"
        plec = "Mężczyzna" if self.chlop.isChecked() else "Kobieta"
        wojewodztwo = self.woj_input.currentText()

        zainteresowania = []
        if self.zain1.isChecked():
            zainteresowania.append("Gry")
        if self.zain2.isChecked():
            zainteresowania.append("Muzyka")

        print(f"Imię: {imie}, Nazwisko: {nazwisko}, PESEL: {pesel}")
        print(f"Kod pocztowy: {kod_pocztowy}, Płeć: {plec}, Województwo: {wojewodztwo}")
        print(f"Zainteresowania: {', '.join(zainteresowania)}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())