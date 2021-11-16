from modules import sqLite


# Find and delete btn
def delete_btn(index: int, text_btn: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    all_btns = str(project_line[4])
    new_text_btns = ""
    rows = all_btns.split("#@#")
    for i in rows:
        btn_s = str(i).split("@$@")
        for k in btn_s:
            if str(k) == text_btn or str(k) == '':
                pass
            else:
                new_text_btns = new_text_btns + str(k) + "@$@"
        new_text_btns = new_text_btns + "#@#"
    new_text_btns = new_text_btns.split("#@#")
    finish_text = ''
    for n in new_text_btns:
        if str(n) == '':
            pass
        else:
            finish_text = finish_text + str(n) + "#@#"
    sqLite.insert_info(table='project', name='btn', data=finish_text, id_name="id",
                       telegram_id=index)


# Find and change btn name
def change_btn_name(index: int, text_btn: str, new_text: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    all_btns = str(project_line[4])
    new_text_btns = ""
    rows = all_btns.split("#@#")
    for i in rows:
        btn_s = str(i).split("@$@")
        for k in btn_s:
            if str(k) == '':
                pass
            elif str(k) == text_btn:
                new_text_btns = new_text_btns + new_text + "@$@"
            else:
                new_text_btns = new_text_btns + str(k) + "@$@"
        new_text_btns = new_text_btns + "#@#"
    new_text_btns = new_text_btns.split("#@#")
    finish_text = ''
    for n in new_text_btns:
        if str(n) == '':
            pass
        else:
            finish_text = finish_text + str(n) + "#@#"
    sqLite.insert_info(table='project', name='btn', data=finish_text, id_name="id",
                       telegram_id=index)
    btn_menu_index = sqLite.read_values_by_name(table='project', id_name='in_text', data=text_btn)[0]
    sqLite.insert_info(table='project', name='in_text', data=new_text, id_name="id",
                       telegram_id=btn_menu_index)


# Переместить кнопку вверх
def upp_btn(index: int, text_btn: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    rows = str(project_line[4]).split("#@#")
    new_text_btns = ""
    this_row = None
    solo_row = None
    for i in range(0, (len(rows))):
        btn_s = str(rows[i]).split('@$@')
        if str(rows[i]) != '':
            for k in range(0, (len(btn_s) - 1)):
                if str(btn_s[k]) == text_btn:
                    this_row = i
                    if len(btn_s) - 1 > 1:
                        solo_row = False
                    elif len(btn_s) - 1 == 1:
                        solo_row = True
                    break
                else:
                    pass
    if this_row is not None:
        if (this_row == 0) and solo_row:
            new_text_btns = str(project_line[4])
        elif (this_row == 0) and (not solo_row):
            new_text_btns = text_btn + '@$@#@#'
            for i in range(0, (len(rows) - 1)):
                btn_s = str(rows[i]).split('@$@')
                for k in range(0, (len(btn_s) - 1)):
                    if str(btn_s[k]) == text_btn:
                        pass
                    elif str(btn_s[k]) == '':
                        pass
                    else:
                        new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                new_text_btns = new_text_btns + '#@#'
        elif solo_row:
            for i in range(0, (len(rows) - 1)):
                if (i + 1) == (len(rows) - 1):  # РАссматриваем концовку всего файла

                    if (i + 1) == this_row:
                        new_text_btns = new_text_btns + rows[i] + text_btn + '@$@#@#'
                        break
                    elif i == this_row:
                        btn_s = str(rows[i]).split('@$@')
                        for k in range(0, (len(btn_s) - 1)):
                            if str(btn_s[k]) == text_btn:
                                pass
                            else:
                                new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                        break
                    else:
                        new_text_btns = new_text_btns + str(rows[i]) + '#@#'
                        break  #

                elif (i + 1) != this_row:
                    if i == this_row:
                        pass
                    else:
                        new_text_btns = new_text_btns + rows[i] + '#@#'
                elif (i + 1) == this_row:
                    new_text_btns = new_text_btns + rows[i] + text_btn + '@$@#@#'
                else:
                    print('else')
                    pass
        elif not solo_row:
            for i in range(0, (len(rows) - 1)):
                if (i + 1) == (len(rows) - 1):  # РАссматриваем концовку всего файла

                    if (i + 1) == this_row:
                        new_text_btns = new_text_btns + rows[i] + '#@#' + text_btn + '@$@#@#'
                        btn_s = str(rows[i + 1]).split('@$@')
                        for k in range(0, (len(btn_s) - 1)):
                            if str(btn_s[k]) == text_btn:
                                pass
                            else:
                                new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                        new_text_btns = new_text_btns + '#@#'
                        break
                    elif i == this_row:
                        btn_s = str(rows[i]).split('@$@')
                        for k in range(0, (len(btn_s) - 1)):
                            if str(btn_s[k]) == text_btn:
                                pass
                            else:
                                new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                        new_text_btns = new_text_btns + '#@#'
                        break
                    else:
                        new_text_btns = new_text_btns + str(rows[i]) + '#@#'
                        break

                elif (i + 1) != this_row:
                    if i == this_row:
                        btn_s = str(rows[i]).split('@$@')
                        for k in range(0, (len(btn_s) - 1)):
                            if str(btn_s[k]) == text_btn:
                                pass
                            else:
                                new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                        new_text_btns = new_text_btns + '#@#'
                    else:
                        new_text_btns = new_text_btns + rows[i] + '#@#'
                elif (i + 1) == this_row:
                    new_text_btns = new_text_btns + rows[i] + '#@#' + text_btn + '@$@#@#'
                else:
                    print('else_2')
                    pass

    sqLite.insert_info(table='project', name='btn', data=new_text_btns, id_name="id",
                       telegram_id=index)


# Переместить кнопку вниз
def down_btn(index: int, text_btn: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    rows = str(project_line[4]).split("#@#")
    new_text_btns = ""
    this_row = None
    solo_row = None
    for i in range(0, (len(rows))):
        btn_s = str(rows[i]).split('@$@')
        if str(rows[i]) != '':
            for k in range(0, (len(btn_s) - 1)):
                if str(btn_s[k]) == text_btn:
                    this_row = i
                    if len(btn_s) - 1 > 1:
                        solo_row = False
                    elif len(btn_s) - 1 == 1:
                        solo_row = True
                    break
                else:
                    pass
    if this_row is not None:
        if (this_row == (len(rows))-2) and solo_row:
            new_text_btns = str(project_line[4])
        elif (this_row == (len(rows))-2) and (not solo_row):
            for i in range(0, (len(rows) - 1)):

                btn_s = str(rows[i]).split('@$@')
                for k in range(0, (len(btn_s) - 1)):
                    if str(btn_s[k]) == text_btn:
                        pass
                    elif str(btn_s[k]) == '':
                        pass
                    else:
                        new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                new_text_btns = new_text_btns + '#@#'
            new_text_btns = new_text_btns + text_btn + '@$@#@#'
        elif solo_row:
            for i in range(0, (len(rows) - 1)):
                if i == this_row:
                    new_text_btns = new_text_btns + text_btn + '@$@'
                else:
                    if str(rows[i]) == '':
                        pass
                    else:
                        new_text_btns = new_text_btns + rows[i] + '#@#'
        elif not solo_row:
            for i in range(0, (len(rows) - 1)):
                if i == this_row:
                    btn_s = str(rows[i]).split('@$@')
                    for k in range(0, (len(btn_s)-1)):
                        if str(btn_s[k]) == '':
                            pass
                        elif str(btn_s[k]) == text_btn:
                            pass
                        else:
                            new_text_btns = new_text_btns + str(btn_s[k]) + '@$@'
                    new_text_btns = new_text_btns + '#@#' + text_btn + '@$@#@#'
                else:
                    new_text_btns = new_text_btns + str(rows[i]) + '#@#'
    sqLite.insert_info(table='project', name='btn', data=new_text_btns, id_name="id",
                       telegram_id=index)


# Переместить кнопку влево
def left_btn(index: int, text_btn: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    rows = str(project_line[4]).split("#@#")
    new_text_btns = ""
    this_row = None
    solo_row = None
    for i in range(0, (len(rows))):
        btn_s = str(rows[i]).split('@$@')
        if str(rows[i]) != '':
            for k in range(0, (len(btn_s) - 1)):
                if str(btn_s[k]) == text_btn:
                    this_row = i
                    if len(btn_s) - 1 > 1:
                        solo_row = False
                    elif len(btn_s) - 1 == 1:
                        solo_row = True
                    break
                else:
                    pass
    if solo_row:
        new_text_btns = str(project_line[4])
    else:
        for i in range(0, len(rows)-1):
            if i == this_row:
                btn_s = str(rows[i]).split("@$@")
                for k in range(0, len(btn_s)-1):
                    if k == 0:
                        if str(btn_s[k]) == text_btn:
                            new_text_btns = new_text_btns + rows[i]
                            break
                        else:
                            if str(btn_s[k]) == '':
                                pass
                            elif str(btn_s[k+1]) == text_btn:
                                new_text_btns = new_text_btns + text_btn + "@$@" + str(btn_s[k]) + "@$@"
                            elif str(btn_s[k]) == text_btn:
                                pass
                            else:
                                new_text_btns = new_text_btns + str(btn_s[k]) + "@$@"
                    else:
                        if str(btn_s[k]) == '':
                            pass
                        elif str(btn_s[k + 1]) == text_btn:
                            new_text_btns = new_text_btns + text_btn + "@$@" + str(btn_s[k]) + "@$@"
                        elif str(btn_s[k]) == text_btn:
                            pass
                        else:
                            new_text_btns = new_text_btns + str(btn_s[k]) + "@$@"
                new_text_btns = new_text_btns + "#@#"
            else:
                new_text_btns = new_text_btns + rows[i] + "#@#"

    sqLite.insert_info(table='project', name='btn', data=new_text_btns, id_name="id",
                       telegram_id=index)


# Переместить кнопку влево
def right_btn(index: int, text_btn: str):
    project_line = sqLite.read_value_table_name(table='project', graph="*", id_name='id', telegram_id=index)
    rows = str(project_line[4]).split("#@#")
    new_text_btns = ""
    this_row = None
    solo_row = None
    for i in range(0, (len(rows))):
        btn_s = str(rows[i]).split('@$@')
        if str(rows[i]) != '':
            for k in range(0, (len(btn_s) - 1)):
                if str(btn_s[k]) == text_btn:
                    this_row = i
                    if len(btn_s) - 1 > 1:
                        solo_row = False
                    elif len(btn_s) - 1 == 1:
                        solo_row = True
                    break
                else:
                    pass
    if solo_row:
        new_text_btns = str(project_line[4])
    else:
        for i in range(0, len(rows)-1):
            if i == this_row:
                btn_s = str(rows[i]).split("@$@")
                for k in range(0, len(btn_s)-1):

                    if str(btn_s[k]) == text_btn:
                        if str(btn_s[k+1]) != '':
                            new_text_btns = new_text_btns + btn_s[k+1] + "@$@" + text_btn + "@$@"
                        else:
                            new_text_btns = new_text_btns + text_btn + "@$@"
                    elif str(btn_s[k]) == '':
                        break
                    else:
                        if str(btn_s[k-1]) == text_btn:
                            pass
                        else:
                            new_text_btns = new_text_btns + btn_s[k] + "@$@"
                new_text_btns = new_text_btns + "#@#"
            else:
                new_text_btns = new_text_btns + rows[i] + "#@#"

    sqLite.insert_info(table='project', name='btn', data=new_text_btns, id_name="id",
                       telegram_id=index)


# Создать сложное меню
def create_menu_btn(text_btn: str):
    sqLite.insert_first_note(table='project', id_name="in_text", telegram_id=text_btn)
    sqLite.insert_info(table='project', name='post', data=f'Текст кнопки {text_btn}', id_name="in_text",
                       telegram_id=text_btn)


# Вырезать кнопку
def cut_btn(index: int, text_btn: str):
    delete_btn(index=index, text_btn=text_btn)


# Перейти наад в меню
def btn_back(in_text: str):
    project = sqLite.read_all(table='project')
    back_window = ''
    for line in project:
        all_btns = str(line[4]).split('#@#')
        for grup_btns in all_btns:
            text_btn = grup_btns.split('@$@')
            for btn in text_btn:
                if str(btn) == in_text:
                    back_window = line[1]
                else:
                    pass
    if (back_window is None) or (back_window == ''):
        return 'Главное_Меню'
    else:
        return back_window


# Сохранение данных опроса создание/очистка файла:
def start_q_a(name: str):
    with open(f'modules/answers/{name}.txt', 'w') as file:
        pass


# Сохранение данных опроса файла:
def save_q_a(name: str, data: str):
    with open(f'modules/answers/{name}.txt', 'a') as file:
        file.write(f'--NEXT ANSWER--{data}')


def post_upp(data: str):
    index = str(data).split('#')[0]
    table = str(data).split('#')[1]
    posts = sqLite.read_all(table=f'post{table}')
    post_id = sqLite.read_values_by_name(table=f'post{table}', data=index, id_name='number')[4]
    index = int(index)
    for k in posts:
        if index - 1 > int(k[0]):
            pass
        elif index - 1 == int(k[0]):
            sqLite.insert_info(table=f'post{table}', name='number', data=str(int(k[0]) + 1), id_name='id',
                               telegram_id=k[4])
            sqLite.insert_info(table=f'post{table}', name='number', data=str(int(k[0])), id_name='id',
                               telegram_id=post_id)
        else:
            pass


def post_down(data: str):
    index = str(data).split('#')[0]
    table = str(data).split('#')[1]
    posts = sqLite.read_all(table=f'post{table}')
    post_id = sqLite.read_values_by_name(table=f'post{table}', data=index, id_name='number')[4]
    index = int(index)
    for k in posts:
        if index + 1 > int(k[0]):
            pass
        elif index + 1 == int(k[0]):
            sqLite.insert_info(table=f'post{table}', name='number', data=str(int(k[0])-1), id_name='id',
                               telegram_id=k[4])
            sqLite.insert_info(table=f'post{table}', name='number', data=str(int(k[0])), id_name='id',
                               telegram_id=post_id)
        else:
            pass


def re_build(table: str):
    new_number = 1
    i = 1
    while i < 100:
        try:
            post_id = sqLite.read_values_by_name(table=f'post{table}', data=i, id_name='number')[4]
            sqLite.insert_info(table=f'post{table}', name='number', data=new_number, id_name='number',
                               telegram_id=i)
            i += 1
            new_number += 1
        except:
            i += 1
