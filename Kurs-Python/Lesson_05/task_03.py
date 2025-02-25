def calculate_area(length, width):
    area = length * width
    return area

storage_length = 28
storage_width = 12
table_length = 4
table_width = 2

storage_area = calculate_area(storage_length, storage_width)
table_area = calculate_area(table_length, table_width)
tables = storage_area // table_area

print("На склад поместится", tables, "столов")
