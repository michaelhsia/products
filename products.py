products = []
while True: #while適用於不知道使用者會執行幾次迴圈
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

#p = [] 必須放在while loop 中, 否則會一直累加上去
#p.append(name)
#p.append(price)
#products.append(p)

#p = [name, price] 等於 10-12 行

#products = append([name, price]) 等於 10-13 行