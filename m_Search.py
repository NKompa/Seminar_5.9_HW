def Search_Entry(search_info):
    list_result = []
    # count = 0
    with open('phonebook.csv',encoding='utf-8') as book:
        for line in book:
            if search_info in line:
                list_result.append(line)
                # count+=1
    return list_result
    # if count==0:
    #     return 'Таких данных нет.'