month = int(input("Введите номер месяца:"))
list_month = ["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
print(f"Сезон месяца {list_month[month-1]}")

dict_month = {1:"Зима",2:"Зима",3:"Весна",4:"Весна",5:"Весна",6:"Лето",7:"Лето",8:"Лето",9:"Осень",10:"Осень",11:"Осень",12:"Зима"}
print(f"Сезон месяца {dict_month[month]}")