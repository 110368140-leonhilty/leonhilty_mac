menu = {
    '三明治' : 50,
    '咖啡'  : 40,
    '沙拉'  : 30
}
def order_meal():
    total = 0
    while order := input('請點餐：'):
        if order in menu:
            price = menu[order]
            total += price
            print(f'{order} {total}元,總經額為{total}')
        else :
            print(f'抱歉！我們沒有提供{order}')
    print(f'您的帳單為{total}元')
    
order_meal()




