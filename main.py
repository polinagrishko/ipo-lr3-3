day =int(input("введите день:"))
month = int(input("введите месяц:"))
if(month == 3 and day >=1)or (month ==4)or(month ==5)or (month==6 and day <=31):
    season ="весна"
elif (month ==6 and day >=1) or (month ==7) or (month ==8)or (month ==8 and day <=31):
    season ="лето"
elif (month ==9 and day>=1) or (month==10) or (month ==11 and day<=30):
    season ="зима"
    print(f"дата{day}.{month} относится к сезону:{season}")