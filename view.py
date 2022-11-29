def All_view():
    list1 = []
    with open('phonebook.csv', encoding='utf-8') as book:
        for line in book:
            list1.append(line.replace(',', ''))
        return list1

def Web_view():
    with open('phonebook.csv', encoding='utf-8') as book:
        data = book.readlines()
        return data