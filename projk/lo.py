import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

class MojeOkno(QWidget):
    def __init__(self):
        super().__init__()

        self.pole_zgoda = QCheckBox("Zgadzam się")
        self.zgd = QPushButton("Zgadzam się")
        self.niezg = QPushButton("Nie zgadzam się")

        pion = QVBoxLayout()
        poz = QHBoxLayout()

        poz.addWidget(self.zgd)
        poz.addWidget(self.niezg)

        pion.addWidget(self.pole_zgoda, alignment=Qt.AlignmentFlag.AlignCenter)
        pion.addLayout(poz)

        self.zgd.clicked.connect(self.klik_zgadzam)
        self.niezg.clicked.connect(self.klik_nie_zgadzam)

        self.setLayout(pion)
        self.setWindowTitle("Checkbox Demo")
        self.setGeometry(300, 300, 300, 200)

    def klik_zgadzam(self):
        self.pole_zgoda.setChecked(True)

    def klik_nie_zgadzam(self):
        self.pole_zgoda.setChecked(False)


if __name__ == "__main__":
    aplikacja = QApplication(sys.argv)
    okno = MojeOkno()
    okno.show()
    sys.exit(aplikacja.exec())
