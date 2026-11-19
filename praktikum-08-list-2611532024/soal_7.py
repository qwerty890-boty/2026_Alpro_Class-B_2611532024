menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# 1. Baca data dengan nested loop
for day in range(number_of_days):
    daily_sales = []
    for menu in menus:
        qty = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(qty)
    sales.append(daily_sales)
  
# 2. Cetak total porsi setiap hari
print("Total per day:")
for day in range(number_of_days):
    day_total = 0
    for col in range(len(menus)):
        day_total += sales[day][col]
    print(f"Day {day + 1}: {day_total}")
  
# 3. Hitung total setiap menu
menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for day in range(number_of_days):
        menu_total += sales[day][col]
    menu_totals.append((menus[col], menu_total))
print(f"Total per menu: {menu_totals}")

# 4. Cari menu terlaris
best_menu = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_menu = name
print(f"Best seller: {best_menu} ({best_total})")
