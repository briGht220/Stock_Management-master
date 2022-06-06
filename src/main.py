import tkinter
import tkinter.messagebox

# 모듈 임포트  
from module.Stock import Stock
from module.StockList import StockList
from module.StockManage import StockManage


# 윈도우 화면 초기화  
def windowInit() -> tkinter.Tk:
    root = tkinter.Tk()
    root.geometry('1000x500+300+100')
    root.title('Stock Management')

    return root


def insertDataCommand(stock: Stock) -> None:
    StockManage.appendStock(stock)
    tkinter.messagebox.showinfo('Info', 'Data Inserted')
    showAllData()


# 데이터를 추가하는 함수  
def insertData() -> None:
    global root

    # 새로운 윈도우 생서
    insertWindow = tkinter.Toplevel(root)
    insertWindow.geometry('300x300')
    insertWindow.title('InsertData')

    # frame 선언 부
    frameleft = tkinter.Frame(insertWindow)
    frameleft.pack(side='left', fill='y')

    # 새로운 윈도우의 버튼, 라벨 생성
    tkinter.Label(frameleft, text='Stock Name').pack(fill='x', padx=10, pady=10)
    nameEntry = tkinter.Entry(insertWindow)
    tkinter.Label(frameleft, text='Stock Count').pack(fill='x', padx=10, pady=10)
    countEntry = tkinter.Entry(insertWindow)
    tkinter.Label(frameleft, text='Stock Limit').pack(fill='x', padx=10, pady=10)
    limitEntry = tkinter.Entry(insertWindow)
    tkinter.Label(frameleft, text='Stock In Day').pack(fill='x', padx=10, pady=10)
    inDayEntry = tkinter.Entry(insertWindow)
    tkinter.Label(frameleft, text='Stock Out Day').pack(fill='x', padx=10, pady=10)
    outDayEntry = tkinter.Entry(insertWindow)
    tkinter.Label(frameleft, text='Stock Company').pack(fill='x', padx=10, pady=10)
    companyEntry = tkinter.Entry(insertWindow)

    # entry 붙여넣기
    nameEntry.pack(fill='x', padx=10, pady=11)
    countEntry.pack(fill='x', padx=10, pady=11)
    limitEntry.pack(fill='x', padx=10, pady=11)
    inDayEntry.pack(fill='x', padx=10, pady=11)
    outDayEntry.pack(fill='x', padx=10, pady=11)
    companyEntry.pack(fill='x', padx=10, pady=11)

    tkinter.Button(insertWindow, text='Insert Data', command=lambda: insertDataCommand(Stock(
        nameEntry.get(),
        countEntry.get(),
        limitEntry.get(),
        inDayEntry.get(),
        outDayEntry.get(),
        companyEntry.get()
    ))).pack(side='bottom', padx=10, pady=10)


def deleteDataCommand(index: str) -> None:
    try:
        index_num = int(index)
    except:
        tkinter.messagebox.showerror('Value Error', 'Check value type (index : int)')
        return

    StockManage.deleteStock(index_num)
    tkinter.messagebox.showinfo('Info', 'Data Deleted')
    showAllData()


def deleteData() -> None:
    global root

    # 새로운 윈도우 생서
    deleteWindow = tkinter.Toplevel(root)
    deleteWindow.geometry('300x100+300+300')
    deleteWindow.title('DeleteData')

    # frame 선언 부
    frameleft = tkinter.Frame(deleteWindow)
    frameleft.pack(side='left', fill='y')

    # label, entry 생성 부
    tkinter.Label(frameleft, text='Index').pack(fill='x', padx=10, pady=10)
    indexEntry = tkinter.Entry(deleteWindow)
    indexEntry.pack(fill='x', padx=10, pady=11)

    #버튼 생성
    tkinter.Button(deleteWindow, text='Delete Data', command=lambda: deleteDataCommand(indexEntry.get())).pack(side='bottom', padx=10, pady=10)


# 데이터를 텍스트 화면에 띄어주는 함수
def showAllData() -> None:
    global textShowData
    classOBJ = ('Name', 'Count', 'Limit_day', 'In_day', 'Out_day', 'Company')

    slist = StockList.getStockList()
    line = ''

    for i in slist:
        stock = i.returnByList()
        cnt = 0

        for j in stock:
            line += classOBJ[cnt] + ': %7s  |  ' %(j)
            cnt += 1
        
        line += '\n'

    textShowData.configure(state='normal')
    textShowData.delete(1.0, tkinter.END)
    textShowData.insert(1.0, line)
    textShowData.configure(state='disable')


# 프로그램을 종료하는 함수  
def tkinterClose():
    global root
    root.destroy()


# 메인  
if __name__ == '__main__':
    # 프로그램을 시작하며, 데이터 파일에 있는 데이터 가져옴  
    StockList.getDataFromDatabase()

    # 메인 프레임 (window) 초기화  
    root = windowInit()

    # 왼쪽 프레임  
    frameleft = tkinter.Frame(root)
    frameleft.pack(side='left')

    # 버튼  
    buttonShowList = tkinter.Button(frameleft, text='Show All List', command=showAllData)
    buttonInsert = tkinter.Button(frameleft, text='Insert data', command=insertData)
    buttonQuit = tkinter.Button(frameleft, text='Exit Programm', command=tkinterClose)
    buttonDelete = tkinter.Button(frameleft, text='Delete data', command=deleteData)

    # 스크롤 바 
    yscroll = tkinter.Scrollbar(root)
    xscroll = tkinter.Scrollbar(root, orient='horizontal')
    yscroll.pack(side='right', fill='y')
    xscroll.pack(side='bottom', fill='x')

    # 텍스트 ( 데이터 보여주는 부분 )
    textShowData = tkinter.Text(root, height=80, yscrollcommand=yscroll.set, xscrollcommand=xscroll.set, state='disable')
    yscroll.config(command=textShowData.yview)
    xscroll.config(command=textShowData.xview)

    # 버튼 커맨드 설정  

    # 붙여넣기 부분  
    buttonShowList.pack(side='top', fill='x', padx=10, pady=10)
    buttonInsert.pack(side='top', fill='x', padx=10, pady=10)
    buttonDelete.pack(side='top', fill='x', padx=10, pady=10)
    buttonQuit.pack(side='bottom', fill='x', padx=10, pady=10)
    textShowData.pack(anchor='center', fill='both')

    showAllData()
    root.mainloop()
