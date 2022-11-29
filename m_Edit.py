def Edit_Entry(sirname_edit,element_number,element_new):

    sirname = sirname_edit
    lines = []

    with open('phonebook.csv', encoding="utf-8") as data:
        for line in data:
            if not sirname in line:
                lines += line
            else:
                line = line.split(", ")
                old = element_number-1
                new = element_new
                line[old] = new
                line = ", ".join(line)
                lines += line

    with open('phonebook.csv', 'w', encoding="utf-8") as data:
        data.writelines(lines)