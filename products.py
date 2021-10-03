products = []
while True: #while適用於不知道使用者會執行幾次迴圈
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

#p = [] 必須放在while loop 中, 否則會一直累加上去
#p.append(name)
#p.append(price)
#products.append(p)

#p = [name, price] 等於 10-12 行

#products = append([name, price]) 等於 10-13 行

with open ('products.csv', 'w', encoding='utf-8') as f: #加入utf-8(最廣泛使用的編碼), 才能正常讀取/寫入) 
                                                        #寫入檔案, 如果資料夾中沒有會建立檔案, 如果有同樣檔案會覆蓋
    f.write('商品, 價格\n') #','用來分隔csv檔中的每個標題
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #字串可用 '+', '*'來合併
                                          #'a' + 'b' = 'ab', 'abc' * 3 = 'abcabcabc'





