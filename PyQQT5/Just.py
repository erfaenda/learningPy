from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Первая программа на PyQt')
window.resize(300, 70)
lable = QtWidgets.QLabel('<center>Привет мир!</center')
btnQuit = QtWidgets.QPushButton('&Закрыть окно')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(lable)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())