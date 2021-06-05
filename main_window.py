import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from database_info.database_user import database1

a = QApplication(sys.argv)
r = QWidget()
background = QLabel(r)
pix = QPixmap('img/bg.jpg')
background.setPixmap(pix)
r.setGeometry(100, 100, 736, 491)
# two edit line
user = QLabel('Username:', r)
passd = QLabel('Password:', r)
user.move(200, 150)
passd.move(200, 180)
username = QLineEdit(r)
password = QLineEdit(r)
username.move(300, 150)
password.move(300, 180)
# two button
signin = QPushButton('Sign in', r)
signin.move(300, 220)
signup = QPushButton('Sign up', r)
signup.move(400, 220)


def ev1():
    var = database1().check_user(username.text(), password.text())
    if var == 1:
        print('OK')
        ty = database1().get_status(username.text())
        if ty == 'student':
            import student.main_stu
        else:
            r.destroy()
            import professor.main_pro
    elif var == 2:
        username.setText('')
        password.setText('')
        print('Password is wrong')
    else:
        username.setText('')
        password.setText('')
        print('User is not exist')


def ev2():
    import sec_window


signin.clicked.connect(ev1)
signup.clicked.connect(ev2)
r.show()
sys.exit(a.exec_())
