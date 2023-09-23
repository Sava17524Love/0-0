from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Crazy People')
win.resize(400,200)

question = QLabel(win)
question.setText('Якого року канал отимав золоту кнопку від Ютуб?')
question.move(50, 10)

button1 = QRadioButton(win)
button1.setText('2005')
button1.move(100, 60)

button2 = QRadioButton(win)
button2.setText('2010')
button2.move(200, 60)

button3 = QRadioButton(win)
button3.setText('2015')
button3.move(100, 120)

button4 = QRadioButton(win)
button4.setText('2020')
button4.move(200, 120)

def show_win():
    win2 = QMessageBox()
    win2.setText('Правильно! Ви виграли гіроскутер')
    win2.exec_()

def show_lose():
    win2 = QMessageBox()
    win2.setText('ні, в 2015 році. Ви виграли фірмовий плакат')
    win2.exec_()

button1.clicked.connect(show_lose)
button2.clicked.connect(show_lose)
button3.clicked.connect(show_win)
button4.clicked.connect(show_lose)

win.show()
app.exec_()
