products = []
while True:
    product = input('請輸入品名：')
    if product == 'q':
        break
    price = input('請輸入價格：')
    products.append([product, price])

for each in products:
    print(each)
