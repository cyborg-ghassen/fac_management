import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton
from PyQt5.QtGui import QPixmap
from database_info.database_user import database1
a = QApplication(sys.argv)
t = QWidget()
background = QLabel(t)
pix = QPixmap('img/bg.jpg')
background.setPixmap(pix)
t.setGeometry(200, 200, 736, 491)
# five labels
fullName = QLabel('Full name', t)
passW = QLabel('Password', t)
filiere = QLabel('Filiere', t)
depart = QLabel('Department', t)
type = QLabel('Type', t)
fullName.move(150, 100)
passW.move(150, 130)
filiere.move(150, 160)
depart.move(150, 190)
type.move(150, 220)
# three edit lines
fullname = QLineEdit(t)
password = QLineEdit(t)
fullname.move(250, 100)
password.move(250, 125)
filiere = QComboBox(t)
filiere.addItem('PC')
filiere.addItem('MP')
filiere.addItem('PT')
filiere.move(250, 150)
# combobox department
department = QComboBox(t)
department.addItem('Chemistry')
department.addItem('Math & IT')
department.addItem('Physics')
department.addItem('STI')
department.move(250, 190)
# type radiobutton
r = QRadioButton('Student', t)
p = QRadioButton('Professor', t)
r.move(200, 230)
p.move(280, 230)
# button
send = QPushButton('Send data', t)
send.move(200, 270)


def ev3():
    f = fullname.text()
    pa = password.text()
    u = filiere.currentText()
    if r.isChecked():
        tt = 'student'
    elif p.isChecked():
        tt = 'professor'
    else:
        tt = 'null'
    d = department.currentText()
    database1().insert_data(f, pa, u, tt, d)
    print('Done')
    t.destroy()


send.clicked.connect(ev3)
t.show()
