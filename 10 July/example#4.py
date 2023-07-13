orders = [ {'product':'apple','quantity':500}, 
           {'product':'banana','quantity':300}, 
           {'product':'apple','quantity':200}, 
           {'product':'orange','quantity':400}, 
           {'product':'banana','quantity':1000}]

product_quantity = {}
for order in orders: 
    product = order['product'] 
    quantity = order['quantity']
    if product in product_quantity: 
        product_quantity[product] += quantity
    else: 
        product_quantity[product] = quantity

for product, quantity in product_quantity.items():
    print(f'{product}:{quantity}')
