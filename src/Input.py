import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import CalScoreModule as CalScoreModule
from CompareCompany import SecondWindow




form_class = uic.loadUiType("./UI/InputPage.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Scorebutton.clicked.connect(self.CalculateScore)
        self.Nextbutton.clicked.connect(self.NextModal)
        self.weights:list =  [0.3, 0.3, 0.3, 0.1] # 가중치
        self.setTextReadOnly()

        self.UserData = ['', [], 0]

    def setTextReadOnly (self) :
        self.Score1.setReadOnly(True)
        self.Score2.setReadOnly(True)
        self.Score3.setReadOnly(True)
        self.Score4.setReadOnly(True)
        self.Score5.setReadOnly(True)
        self.Score6.setReadOnly(True)
        self.Score7.setReadOnly(True)

        self.InputName1.setReadOnly(True)
        self.InputName2.setReadOnly(True)
        self.InputName3.setReadOnly(True)
        self.InputName4.setReadOnly(True)
        self.InputName5.setReadOnly(True)
        self.InputName6.setReadOnly(True)

        self.LABEL1.setReadOnly(True)
        self.LABEL2.setReadOnly(True)
        self.LABEL3.setReadOnly(True)

    def CalculateScore (self) :

        UserData:list = [
            self.Input1.toPlainText(),
            self.Input2.toPlainText(),
            self.Input3.toPlainText(),
            self.Input4.toPlainText(),
            self.Input5.toPlainText(),
            self.Input6.toPlainText(), 
        ]
        UserData = CalScoreModule.inputUserData(UserData, self.weights)

        self.Score1.setPlainText(str(UserData[0]))
        self.Score2.setPlainText(str(UserData[1][0]))
        self.Score3.setPlainText(str(UserData[1][1]))
        self.Score4.setPlainText(str(UserData[1][2]))
        self.Score5.setPlainText(str(UserData[1][3]))
        self.Score6.setPlainText(str(UserData[1][4]))
        self.Score7.setPlainText(str(UserData[2]))

        self.UserData = UserData


    # 주문 완료 화면 실행
    def NextModal(self):
        self.hide() #메인 윈도우 숨김
        self.second = SecondWindow(self.UserData, self.weights)
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()