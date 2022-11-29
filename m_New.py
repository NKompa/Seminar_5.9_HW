def New_Entry(list):
    new_sirname = list[0]
    new_name = list[1]
    new_phone = list[2]
    new_comment = list[3]
    with open('phonebook.csv','a', encoding='utf-8') as book:
        book.write(f'{new_sirname}, {new_name}, {new_phone}, {new_comment};\n')