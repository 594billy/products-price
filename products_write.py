import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            else:
                product, price = line.strip().split(',')
                products.append([product, price])      
    return products


#輸入新資料
def user_input(products):
    while True:
        product = input('請輸入品名：')
        if product == 'q':
            break
        price = input('請輸入價格：')
        products.append([product, price])
    return products

#印出所有資料
def print_products(products):
    for each in products:
        print(each[0], '的價格是', each[1])

#寫入資料
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        f.write('商品,價格\n')
        for each in products:
            f.write(each[0] + ',' + each[1] + '\n')


def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('已讀取檔案')
        products = read_file(filename)
    else:
        print('無紀錄')
        products = []
    
    products = user_input(products)
    print_products(products)
    write_file('product.csv', products)

main()
