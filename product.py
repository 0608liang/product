products = []

while True : 
	name = input('請輸入商品名稱 : ')
	if name == 'q' : 
		break
	price = input('請輸入商品價格 : ')
	products.append([name, price])

for p in products : 
	print(f"商品名稱 : {p[0]} \t商品價格 : {p[1]}")