#讀取檔案
products = []
with open('product.csv', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        else:
            product, price = line.strip().split(',')
            products.append([product, price])
print(products)

#輸入新資料
while True:
    product = input('請輸入品名：')
    if product == 'q':
        break
    price = input('請輸入價格：')
    products.append([product, price])

#印出所有字料
for each in products:
    print(each[0], '的價格是', each[1])

#寫入資料
with open('product.csv', 'w', encoding = 'utf-8-sig') as f:
    f.write('商品,價格\n')
    for each in products:
        f.write(each[0] + ',' + each[1] + '\n')