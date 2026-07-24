def clean_price(price_str):
    cleaned=price_str.replace('$','').replace(',','')
    return float(cleaned)

def normaliz_score(score,max_score=100):
    return round((score/max_score)*100,2)

price=clean_price("$1,999.00")
print(f"Cleaned price: {price}")

percentage_1=normaliz_score(54,60)
percentage_2=normaliz_score(78)

print(f"54/60 as a percentage: {percentage_1}%")
print(f"76/100 as a percentage: {percentage_2}%")
