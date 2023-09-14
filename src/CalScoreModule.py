    
import openpyxl # openpyxl 모듈 선언 

### 데이터 로드 함수 (return : dict)
def load_database () -> dict: # dictionary를 반환하는 함수 선언

    filename:str = "DataBase.xlsx" #파일명
    book:openpyxl.load_workbook = openpyxl.load_workbook(filename) #엑셀파일 book 변수에 저장
    sheet=book.worksheets[0] #첫번쨰 워크시트

    data:dict = {}
    for row in sheet.rows: #전체 행에 대하여 반복
        data[row[0].value] = [ # 1열 데이터 (회사명)
            row[1].value, # 2열 데이터 (매출액 증가율)
            row[2].value, # 3열 데이터 (이자 보상 배율)
            row[3].value, # 4열 데이터 (ROA)
            row[4].value, # 5열 데이터 (지속 가능 경영 여부)
            row[5].value  # 6열 데이터 (무디스 평가 점수)
    ] 
    
    return data

### 점수를 계산하는 함수 (return : dict)
def calculate_score (weights:dict, data:dict) -> dict: # dictionary를 반환하는 함수 선언
    scoreData:dict = {}
    for key, value in data.items(): # key, value 값을 dictonary로부터 받아옴.
        ScoreDataList:list = []
        ScoreDataList.append(round(value[0] * weights [0],1)) # 매출액 증가율
        ScoreDataList.append(round(value[1] * weights [1],1)) # 이자 보상 배율
        ScoreDataList.append(round(value[2] * weights [2],1)) # ROA
        if value[3] == 'O' : # 지속 가능 경영 여부
            ScoreDataList.append(10)
        else :
            ScoreDataList.append(0)
        ScoreDataList.append(round(value[4] * weights [3],1)) # 무디스 평가 점수

        
        scoreData[key] = [key, ScoreDataList, round(sum(ScoreDataList), 1)] # 둘째 자리에서 반올림
    return scoreData

#['매출액 증가율', '이자 보상 배율', 'ROA', '지속 가능 경영 여부', '무디스 평가 점수']

### 사용자의 데이터를 받아서 점수를 반환하는 함수
def inputUserData (Data:list, weights:list) -> list:
    UserCompanyName:str = Data[0]
    ScoreData:list = []

    ScoreData.append(float(Data[1]) * weights [0]) # 매출액 증가율
    ScoreData.append(float(Data[2]) * weights [1]) # 이자 보상 배율
    ScoreData.append(float(Data[3]) * weights [2]) # ROA
    if Data[4] == 'O' : # 지속 가능 경영 여부
        ScoreData.append(10)
    else :
        ScoreData.append(0)
    ScoreData.append(float(Data[5]) * weights [3]) # 무디스 평가 점수

    return [UserCompanyName, ScoreData, round(sum(ScoreData),1)]

#DataBase:dict = load_database() # 데이터
#ScoreDict:dict = calculate_score(weights, DataBase) # 점수 데이터
#sorted_score_dict:dict = dict(sorted(ScoreDict.items(), key=lambda x : x[1], reverse=True)) # 정렬된 점수 데이터
#Data = inputUserData()




