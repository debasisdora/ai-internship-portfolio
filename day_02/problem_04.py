products=[
    {"name":"laptop","stock":5},
    {"name":"mouse","stock":0},
    {"name":"keyboard","stock":3},
    {"name":"moniter","stock":0}
]
out_of_stock=[product["name"] for product in products if product["stock"]==0]
print(out_of_stock)