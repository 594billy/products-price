products = []
while True:
    product = input('請輸入品名：')
    if product == 'q':
        break
    price = input('請輸入價格：')
    info = [product, price]
    products.append(info)

for each in products:
    print(each)
