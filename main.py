day =int(input("введите день:")) #вывод данной надписи на консоль
month = int(input("введите месяц:")) # вывод даной надписи на консоль
if(month == 3 and day >=1)or (month ==4)or(month ==5)or (month==6 and day <=31):#условие для определения определенного сезона
    season ="весна"
elif (month ==6 and day >=1) or (month ==7) or (month ==8)or (month ==8 and day <=31): # условие для определения определенного сезона
    season ="лето"
elif (month ==9 and day>=1) or (month==10) or (month ==11 and day<=30): # условие для определения опредленного сезона
    season ="зима"
    print(f"дата{day}.{month} относится к сезону:{season}") # вывод конкретного сезона на консоль
