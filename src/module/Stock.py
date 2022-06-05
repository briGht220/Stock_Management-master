# 재고 저장할 클래스
class Stock:
    # 상품명
    stock_Name = None
    # 수량
    stock_Count = None
    # 유통기한
    stock_Limit = None
    # 입고일
    stock_In_Day = None
    # 출고 예정일
    stock_Out_Day = None
    # 제조사명
    stock_Company = None

    def __init__(self, sN: str, sC: str, sL: str, sI: str, sO: str, sCom: str) -> None:
        self.stock_Name = sN
        self.stock_Count = sC
        self.stock_Limit = sL
        self.stock_In_Day = sI
        self.stock_Out_Day = sO
        self.stock_Company = sCom


    # class를 리스트로 반환해주는 함수
    def returnByList(self) -> list:
        return [self.stock_Name, self.stock_Count, self.stock_Limit, self.stock_In_Day, self.stock_Out_Day, self.stock_Company]


# 메인  
if __name__ == '__main__':
    pass
