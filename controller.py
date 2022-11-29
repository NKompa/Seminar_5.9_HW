import view
import m_New
import m_Search
import m_Edit
import m_Delete
import telebot

bot = telebot.TeleBot(TOKEN)

new_person = []

@bot.message_handler(commands=['start'])
def Show_Menu(message):
    bot.send_message(message.chat.id, f"Меню:\n1. Добавить новый контакт\n2. Посмотреть все контакты\n3. Найти контакт\n4. Изменить контакт\n5. Удалить контакт")

@bot.message_handler(content_types=['text'])
def Controller(message):
    choice = message.text
    if choice == '1':
        bot.send_message(message.chat.id, 'Введите фамилию')
        bot.register_next_step_handler(message, Get_Sirname)
    if choice == '2':
        phone_list = view.All_view()
        for i in phone_list:
            bot.send_message(message.chat.id, i)
        Show_Menu(message)
        bot.register_next_step_handler(message,Controller)
    if choice == '3':
        bot.send_message(message.chat.id, 'Что ищем?')
        bot.register_next_step_handler(message, Find_Entry)
    if choice == '4':
        bot.send_message(message.chat.id, 'Введите фамилию для изменения')
        bot.register_next_step_handler(message, Sirname_Edit)
    if choice == '5':
        bot.send_message(message.chat.id, 'Введите фамилию для удаления')
        bot.register_next_step_handler(message, Delete)


def Get_Sirname(message):
    new_sirname = message.text
    global new_person
    new_person.append(new_sirname)
    bot.send_message(message.chat.id, 'Введите имя')
    bot.register_next_step_handler(message,Get_Name)

def Get_Name(message):
    new_name = message.text
    global new_person
    new_person.append(new_name)
    bot.send_message(message.chat.id, 'Введите номер телефона')
    bot.register_next_step_handler(message,Get_Phone)

def Get_Phone(message):
    new_phone = message.text
    global new_person
    new_person.append(new_phone)
    bot.send_message(message.chat.id, 'Введите комментарий')
    bot.register_next_step_handler(message,Get_Comment)

def Get_Comment(message):
    new_comment = message.text
    global new_person
    new_person.append(new_comment)
    m_New.New_Entry(new_person)
    new_person = []
    bot.send_message(message.chat.id, 'Новый контакт добавлен.')
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Find_Entry(message):
    search_info = message.text
    result = m_Search.Search_Entry(search_info)
    for i in result:
        bot.send_message(message.chat.id, i)
    if result == []:
        bot.send_message(message.chat.id, 'Таких данных нет.')
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Sirname_Edit(message):
    global sirname_edit
    sirname_edit = message.text
    bot.send_message(message.chat.id, 'Введите номер элемента')
    bot.register_next_step_handler(message, Element_Number)

def Element_Number(message):
    global element_number
    element_number = int(message.text)
    bot.send_message(message.chat.id, 'Введите новое значение')
    bot.register_next_step_handler(message, Element_New)

def Element_New(message):
    global element_new
    element_new = message.text
    m_Edit.Edit_Entry(sirname_edit, element_number, element_new)
    bot.send_message(message.chat.id, 'Изменение выполнено.')
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Delete(message):
    sirname_delete = message.text
    m_Delete.Delete_Entry(sirname_delete)
    bot.send_message(message.chat.id, 'Контакт удалён.')
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

bot.polling(none_stop=True, interval=0)