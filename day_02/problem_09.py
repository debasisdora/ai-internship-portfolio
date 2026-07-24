import csv
highest_revenue=0
best_product=""

with open("sales.csv","r")as file:
    data=csv.DictReader(file)
    for row in data:
        quantity=int(row["quantity"])
        price=float(row["price"])
        revenue=quantity*price
        if revenue > highest_revenue:
            highest_revenue=revenue
            best_product=row["product"]

print(f"Highest revenue product: {best_product}")
print(f"revenue: {highest_revenue}")