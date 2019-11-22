import openpyxl as xl

wb = xl.load_workbook("PokeMartItems.xlsx")
sheet = wb["Sheet1"]
cell = sheet.cell (2, 2)
print(cell.value)

for row in range(3):
    cell = sheet.cell(row, 3)
    product_name = (input("Hello! What item or items would you like to purchase today?: "))
    quantity = int(input(f"How much of {product_name} would you like to buy?: "))
    #have to figure out how to correspond a price with want_to_buy
    print(f"Your total is {total}")
