products = []
while True:
    product = input('請輸入品名：')
    if product == 'q':
        break
    price = input('請輸入價格：')
    products.append([product, price])

for each in products:
    print(each[0], '的價格是', each[1])

with open('prodoct.csv', 'w', encoding = 'utf-8-sig') as f:
    f.write('商品,價格\n')
    for each in products:
        f.write(each[0] + ',' + each[1] + '\n')