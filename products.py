# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品, 價格' in line:
            continue # 直接進入下一個迴圈, 跟break(跳出迴圈)一樣只能在迴圈中出現
        name, price = line.strip().split(',') # strip除去換行符號'\n', .split(',')來用逗點做分割
                                              # split切割完的結果會是'清單'
        products.append([name, price])
print(products)

# 讓使用者輸入
while True: # while適用於不知道使用者會執行幾次迴圈
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# p = [] (必須放在while loop 中, 否則會一直累加上去)
# p.append(name)
# p.append(price)
# products.append(p)

# p = [name, price] 等於 21-24 行

# products = append([name, price]) 等於 21-25 行

# 寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f: # 加入utf-8(最廣泛使用的編碼), 才能正常讀取/寫入) 
                                                        # 寫入檔案, 如果資料夾中沒有, 會建立檔案, 如果有同樣檔案會覆蓋
    f.write('商品, 價格\n') # ','用來分隔csv檔中的每個標題
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 在f(剛剛 open 的檔案), write(自定義的內容)
                                          # 字串可用 '+', '*'來合併
                                          # 'a' + 'b' = 'ab', 'abc' * 3 = 'abcabcabc'





