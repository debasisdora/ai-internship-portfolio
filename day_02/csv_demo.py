import csv
total_revenue=0
row_count=0

with open("sales.csv",'r') as file:
    reader=csv.DictReader(file)

    for row in reader:
        quantity=int(row['quantity'])
        price=float(row['price'])
        line_total=quantity * price
        total_revenue += line_total
        row_count+=1

        print(f"{row['product']}: {quantity} * {price} = ${line_total}")

avg_sale=total_revenue/row_count
print(f" total revenue: {total_revenue}")
print(f"average line-item value: ${round(avg_sale,2)}")