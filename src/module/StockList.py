from . import Stock
import tkinter.messagebox

import os
os.chdir('./database')

# Stock을 저장하는 리스트
class StockList:
    sList = []

    # 데이터를 리스트에 추가하는 함수  
    def appendData(stock: Stock) -> None:
        StockList.sList.append(stock)

    # 데이터베이스로부터 데이터를 가져오는 함수
    def getDataFromDatabase() -> None:
        StockList.sList = []

        try:
            database = open('./data.txt', 'r')
        except:
            tkinter.messagebox.showwarning('Warning', 'There\'s no database. Create new database.')
            database = open('./data.txt', 'w')
            return
        
        data = database.readlines()
        
        for i in data:
            dataLine = i.split()
            try:
                StockList.sList.append(Stock.Stock(dataLine[0], dataLine[1], dataLine[2], dataLine[3], dataLine[4], dataLine[5]))
            except:
                pass

        database.close()

    # sList를 리턴해주는 함수  
    def getStockList() -> None:
        return StockList.sList

    def popStock(index: int) -> None:
        del StockList.sList[index]

