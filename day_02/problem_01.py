def clean_phone_number(raw):
    new_number=raw.replace(" ","").replace("-","").replace("(","").replace(")","").replace("+","")
    if len(new_number)>10:
        return new_number[2:12]
    return new_number

number="+91-9040517254"
print(clean_phone_number(number))
number2="(987) 654-3210"
print(clean_phone_number(number2))
number3="+91 9583315801"
print(clean_phone_number(number3))