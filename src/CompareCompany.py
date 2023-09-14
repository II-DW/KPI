import CalScoreModule as CalScoreModule

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


New = uic.loadUiType(r"./UI/ScorePage.ui")[0] #두 번째창 ui
class SecondWindow(QDialog,QWidget,New):
    def __init__(self, UserData:list, weights:list):
        super().__init__()
        self.setupUi(self)
        self.UserData = UserData
        print(self.UserData)
        self.setStyleSheet("background-color: white;")

        DataBase:dict = CalScoreModule.load_database() # 데이터
        ScoreDict:dict = CalScoreModule.calculate_score(weights, DataBase) # 점수 데이터
        ScoreDict[UserData[0]] = UserData
        sorted_score_dict:dict = dict(sorted(ScoreDict.items(), key=lambda x : x[1][2], reverse=True)) # 정렬된 점수 데이터
        print(ScoreDict)
        self.setTableValues(sorted_score_dict, ScoreDict)
        


    def setTableValues(self, sorted_score_dict:list, DataBase:list) :
        self.table.setRowCount(len(sorted_score_dict))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        i:int = 0
        for key in list(sorted_score_dict.keys()) :
            if key == self.UserData[0] :
                self.table.setItem(i, 0, self.SetItemBackColor(key, (0, 255, 0))) # 회사명
                for n in range (5) :
                    self.table.setItem(i, n+1, self.SetItemBackColor(str(round(DataBase[key][1][n],1)), (0, 255, 0)))
                self.table.setItem(i, 6,self.SetItemBackColor(str(DataBase[key][2]), (0, 255, 0)))
                print(DataBase[key])
            else :
                self.table.setItem(i, 0, self.SetItemColor(key, (0, 0, 0))) # 회사명
                for n in range (5) :
                    RGB = self.SetRGB(float(DataBase[key][1][n]), self.UserData[1][n])
                    self.table.setItem(i, n+1, self.SetItemColor(str(DataBase[key][1][n]), RGB))
                self.table.setItem(i, 6,self.SetItemColor(str(DataBase[key][2]), RGB))

            i+=1
    def SetRGB(self, data:float, userdata:float) -> tuple :
        if data >= userdata :
            return (0, 255, 0)
        else :
            return (255, 0, 0)
    
    def SetItemColor(self, data:str, RGB:tuple) -> QTableWidgetItem :
        item = QTableWidgetItem(data)
        item.setForeground(QBrush(QColor(RGB[0], RGB[1], RGB[2])))
        return item
    
    def SetItemBackColor(self, data:str, RGB:tuple) -> QTableWidgetItem :
        item = QTableWidgetItem(data)
        item.setBackground(QBrush(QColor(RGB[0], RGB[1], RGB[2])))
        return item
            

    