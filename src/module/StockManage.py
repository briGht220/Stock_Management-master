from . import Stock, StockList
import tkinter.messagebox

class StockManage:
    # 객체를 추가하는 함수
    def appendStock(stock: Stock.Stock) -> None:
        StockList.StockList.appendData(stock)

        try:
            appendFile = open('./data.txt', 'a')
        except:
            appendFile = open('./data.txt', 'w')

        stockList = stock.returnByList()
        line = ''

        for i in stockList:
            line += i + ' '
        
        line += '\n'

        appendFile.write(line)
        appendFile.close()

    # 기존의 데이터를 복사하는 함수 (카피 후 이름은 data_old로 고정)
    def cpfile() -> None:
        try:
            oldFile = open('./data.txt', 'r')
            copyFile = open('./data_old.txt', 'w')
        except:
            tkinter.messagebox.showerror('Error', 'File Copy failed')
        
        copyFile.writelines(oldFile.readlines())

        oldFile.close()
        copyFile.close()

    # 데이터를 삭제하는 함수
    def deleteStock(index: int) -> None:
        StockManage.cpfile()
        
        try:
            newFile = open('./data.txt', 'w')
            oldFile = open('./data_old.txt', 'r')
        except:
            tkinter.messagebox.showerror('Error', 'File Open Error')

        old_line = oldFile.readlines()

        for i in range(0, len(old_line)):
            if i == index:
                continue

            newFile.write(old_line[i])
        
        StockList.StockList.popStock(index)
        oldFile.close()
        newFile.close()
