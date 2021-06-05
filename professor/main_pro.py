import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QTableWidget, QTableWidgetItem, QLabel, \
    QPushButton, QLineEdit
from database_info.database_user import database1
from database_info.database_degree import database2

a = QApplication(sys.argv)
t = QMainWindow()
t.setGeometry(100, 100, 736, 491)
tab = QTabWidget(t)
t1 = QWidget()
##################################
#       table for student        #
##################################
table = QTableWidget(t1)
c = database1().get_student()
id = []
fullname = []
type = []
username = []
password = []
department = []
for data in c:
    id.append(data[0])
    fullname.append(data[1])
    password.append(data[2])
    username.append(data[3])
    type.append(data[4])
    department.append(data[5])
table.setColumnCount(6)
table.setRowCount(len(username))
i = 0
while i <= len(username) - 1:
    table.setItem(i, 0, QTableWidgetItem(str(id[i])))
    table.setItem(i, 1, QTableWidgetItem(fullname[i]))
    table.setItem(i, 2, QTableWidgetItem(username[i]))
    table.setItem(i, 3, QTableWidgetItem(type[i]))
    table.setItem(i, 4, QTableWidgetItem(department[i]))
    table.setItem(i, 5, QTableWidgetItem(password[i]))
    i += 1
table.setGeometry(10, 10, 650, 400)
table.setHorizontalHeaderLabels(str("Id:Fullname:UserName:Type:Department:Password").split(":"))
ld = QLabel('Id of student to delete:', t1)
ld.move(50, 430)
e = QLineEdit(t1)
e.move(200, 430)
b = QPushButton('Delete', t1)
b.move(350, 430)


def ev8():
    database1().delete_user(int(e.text()))
    c = database1().get_student()
    id = []
    fullname = []
    type = []
    username = []
    password = []
    department = []
    for data in c:
        id.append(data[0])
        fullname.append(data[1])
        password.append(data[2])
        username.append(data[3])
        type.append(data[4])
        department.append(data[5])
    table.setColumnCount(6)
    table.setRowCount(len(username))
    i = 0
    while i <= len(username) - 1:
        table.setItem(i, 0, QTableWidgetItem(str(id[i])))
        table.setItem(i, 1, QTableWidgetItem(fullname[i]))
        table.setItem(i, 2, QTableWidgetItem(username[i]))
        table.setItem(i, 3, QTableWidgetItem(type[i]))
        table.setItem(i, 4, QTableWidgetItem(department[i]))
        table.setItem(i, 5, QTableWidgetItem(password[i]))
        i += 1


b.clicked.connect(ev8)
#############################
#      second tab           #
#############################
t2 = QWidget()
id = QLabel('id ', t2)
m1 = QLabel('m1', t2)
m2 = QLabel('m2', t2)
m3 = QLabel('m3', t2)
id.move(150, 100)
m1.move(150, 130)
m2.move(150, 160)
m3.move(150, 190)
Id = QLineEdit(t2)
M1 = QLineEdit(t2)
M2 = QLineEdit(t2)
M3 = QLineEdit(t2)
Id.move(250, 100)
M1.move(250, 125)
M2.move(250, 155)
M3.move(250, 185)
add = QPushButton('Add degree', t2)
add.move(350, 250)


def ev4():
    d = database2()
    d.insert_data(int(Id.text()), int(M1.text()), int(M2.text()), int(M3.text()))
    Id.setText('')
    M1.setText('')
    M2.setText('')
    M3.setText('')


add.clicked.connect(ev4)
#############################
#       third tab           #
#############################
t3 = QWidget()
id = QLabel('Enter id of student: ', t3)
m1 = QLabel('M1: ', t3)
m2 = QLabel('M2: ', t3)
m3 = QLabel('M3: ', t3)
m1_d = QLabel('Null', t3)
m2_d = QLabel('Null', t3)
m3_d = QLabel('Null', t3)
id.move(150, 80)
m1.move(150, 110)
m2.move(150, 150)
m3.move(150, 180)
m1_d.move(200, 110)
m2_d.move(200, 150)
m3_d.move(200, 180)
Id1 = QLineEdit(t3)
M11 = QLineEdit(t3)
M21 = QLineEdit(t3)
M31 = QLineEdit(t3)
Id1.move(250, 80)
M11.move(250, 110)
M21.move(250, 150)
M31.move(250, 180)
Id1.resize(50, 20)
M11.resize(50, 20)
M21.resize(50, 20)
M31.resize(50, 20)
search = QPushButton('Search', t3)
update = QPushButton('Update', t3)
search.move(330, 75)
update.move(300, 230)


def ev5():
    data = database2().get_degree(int(Id1.text()))
    if data != None:
        m1_d.setText(str(data[0][1]))
        m2_d.setText(str(data[0][2]))
        m3_d.setText(str(data[0][3]))
    else:
        print("Error")


def ev6():
    database2().update_data(int(Id1.text()), int(M11.text()), int(M21.text()), int(M31.text()))
    m1_d.setText(M11.text())
    m2_d.setText(M21.text())
    m3_d.setText(M31.text())
    M11.setText('')
    M21.setText('')
    M31.setText('')


search.clicked.connect(ev5)
update.clicked.connect(ev6)
tab.resize(736, 491)
#############################
#        fourth tab         #
#############################
t4 = QWidget()
table1 = QTableWidget(t4)
ID = []
FullName = []
Depart = []
D1 = []
D2 = []
D3 = []
sum = []
v = database2().get_degrees()
print(v)
for data in v:
    ID.append(data[0])
    FullName.append(data[1])
    Depart.append(data[2])
    D1.append(data[3])
    D2.append(data[4])
    D3.append(data[5])
    sum.append(data[6])
table1.setColumnCount(7)
table1.setRowCount(len(ID))
i = 0
while i < len(ID):
    table1.setItem(i, 0, QTableWidgetItem(str(ID[i])))
    table1.setItem(i, 1, QTableWidgetItem(FullName[i]))
    table1.setItem(i, 2, QTableWidgetItem(Depart[i]))
    table1.setItem(i, 3, QTableWidgetItem(str(D1[i])))
    table1.setItem(i, 4, QTableWidgetItem(str(D2[i])))
    table1.setItem(i, 5, QTableWidgetItem(str(D3[i])))
    table1.setItem(i, 6, QTableWidgetItem(str(sum[i])))
    i += 1
table1.setGeometry(10, 10, 600, 400)
table1.setHorizontalHeaderLabels(str("Id:Fullname:Department:M1:M2:M3:Sum").split(":"))
refresh = QPushButton('Refresh', t4)
refresh.move(630, 100)


def ev7():
    ID = []
    FullName = []
    Depart = []
    D1 = []
    D2 = []
    D3 = []
    sum = []
    v = database2().get_degrees()
    for data in v:
        ID.append(data[0])
        FullName.append(data[1])
        Depart.append(data[2])
        D1.append(data[3])
        D2.append(data[4])
        D3.append(data[5])
        sum.append(data[6])
    table1.setColumnCount(7)
    table1.setRowCount(len(ID))
    i = 0
    while i < len(ID):
        table1.setItem(i, 0, QTableWidgetItem(str(ID[i])))
        table1.setItem(i, 1, QTableWidgetItem(FullName[i]))
        table1.setItem(i, 2, QTableWidgetItem(Depart[i]))
        table1.setItem(i, 3, QTableWidgetItem(D1[i]))
        table1.setItem(i, 4, QTableWidgetItem(D2[i]))
        table1.setItem(i, 5, QTableWidgetItem(D3[i]))
        table1.setItem(i, 6, QTableWidgetItem(sum[i]))
        i += 1


refresh.clicked.connect(ev7)
tab.addTab(t1, 'Students')
tab.addTab(t2, 'Add Degree')
tab.addTab(t3, 'Update Degree')
tab.addTab(t4, 'Degree')
t.show()
