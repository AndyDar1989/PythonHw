

def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    # print(data_str)
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts


def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    if found_contacts==[]:
        print('Данные не найдены')
        return main_menu()      
    return found_contacts


def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input(
        '1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    else:
        print('Неверный выбор, повторите')
        return ask_search()    
    return search_param, what


def change_contact(file,ch_contact):

    change_pos = input('Выберите пункт, который хотите изменить?: ')
    if change_pos not in '123':
        print('Неверный выбор, повторите')
        return change_contact(file,ch_contact)
    else:
        new_data = input('Внесите изменения: ')
        with open(file, 'r', encoding='utf-8') as data:
            contact = data.readlines()
            with open(file, 'w', encoding='utf-8') as data:
                for i in range(len(contact)):
                    if ch_contact in contact[i]:
                        new_contact = contact[i].split()
                        if change_pos == '1':
                            new_contact[0] = new_data
                        elif change_pos == '2':
                            new_contact[1] = new_data
                        elif change_pos == '3':
                            new_contact[2] = new_data
                        contact[i] = ' '.join(new_contact)
                        data.write(f'{contact[i]}\n')
                    else:
                        data.write(contact[i])           
                        
        #return contact


def delete_contact(file, del_contact):
    #del_contact = input('Хотите удалить?: ')
    with open(file, 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open(file, 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if del_contact not in contact[i]:
                    data.write(contact[i])


def main_menu():
    file_contacts = 'file.txt'
    while True:
        user_choice = input('1 - добавить новый контакт,\n'
                            '2 - найти контакт,\n'
                            '3 - посмотреть весь справочник,\n'
                            '4 - изменить данные контакта,\n'
                            '5 - удалить контакт,\n'
                            '0 - выйти\n')
        if user_choice == '1':
            # print('добавить новый контакт')
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            # print('найти контакт')
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            # print('посмотреть весь справочник')
            print(read_file(file_contacts))
        elif user_choice == '4':
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
            change_contact(file_contacts,what)
            print('Запись изменена')
        elif user_choice == '5':
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)    
            delete_contact(file_contacts,what)
            print('Запись удалена')
        elif user_choice == '0':
            print('До свидания')
            break


if __name__ == '__main__':

    main_menu()
    # # data = ask_user()
    # # print(data)
    # # save_to_file(data, file_contacts)
    # lst_contacts = read_file(file_contacts)
    # print(lst_contacts)
    # search_param, what = ask_search()
    # res = search_contact(lst_contacts, search_param, what)
    # print(res)
    # # lst1 = [1, 2, 3]
    # # lst2 = [7, 8, 9]
    # # res = zip(lst1, lst2)
    # # print(dict(res))
