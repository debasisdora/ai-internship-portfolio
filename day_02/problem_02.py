def apply_discount(price,discount_percentage=10):
    return price*(discount_percentage/100)
price1=800
print(apply_discount(price1,25))
price2=100
print(apply_discount(price2,50))
price3=65
print(apply_discount(price3))