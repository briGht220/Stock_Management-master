from . import Stock, StockList

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
