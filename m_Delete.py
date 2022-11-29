def Delete_Entry(sirname_delete):

    sirname = sirname_delete
    lines = []

    with open('phonebook.csv', encoding="utf-8") as data:
        for line in data:
            if not sirname in line: lines += line
    with open('phonebook.csv', 'w', encoding="utf-8") as data:
            data.writelines(lines)