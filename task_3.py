def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for empl_name in args:
        frst_ltr = empl_name[:1].upper()
        if dict_out.get(frst_ltr) == None :
            new_entry = {frst_ltr: [empl_name]}
            dict_out.update(new_entry)
        else:
            dict_out[frst_ltr].append(empl_name)
    return dict_out


def sort_dict(dict_in: dict) -> dict:
    dict_out = {}
    for ele in sorted(dict_in):
        dict_out[ele] = dict_in[ele]
    return dict_out



names_dict = thesaurus("Иван", "Мария", "Петр", "илья", "Алексей", "Антон", "Ярослав", "Юрий", "Григорий", "Денис")
print(names_dict)
names_dict = sort_dict(names_dict)
print(names_dict)
=======
def convert_list_in_str666(list_in: list) -> str:
    #То что пришло на ум первым
    new_list = []
    for i, st in enumerate(list_in, start=1):
        try:
            numb = int(st)
            if (st[0] == '+') or (st[0] == '-'):
                st = '"{:0=+3d}"'.format(numb)
            else:
                st = '"{:0=2d}"'.format(numb)
        except ValueError:
            numb = 0
        new_list.append(st)
    str_out = ' '.join(new_list)
    return str_out


def is_integer(st: str) -> bool:
    if (st[0] == '+') or (st[0] == '-'):
        st = st[1::]
    return st.isdigit()

def remove_spaces(st: str) -> str:
    i = 0
    qt_open = False
    while i < len(st):
        qt_mark = st.find('"',i)
        if (qt_mark >= 0) and not qt_open:
            i = qt_mark
            st = f"{st[:i+1]}{st[i+2:]}"
            qt_open = True
        elif (qt_mark >= 0) and qt_open:
            i = qt_mark
            st = f"{st[:i-1]}{st[i:]}"
            qt_open = False
        i = i + 1
    return st



def convert_list_in_str(list_in: list) -> str:
    i = 0
    while i < len(list_in):
        st = list_in[i]
        if is_integer(st):
            list_in.insert(i,'"')
            numb = int(st)
            if (st[0] == '+') or (st[0] == '-'):
                st = '{:0=+3d}'.format(numb)
            else:
                st = '{:0=2d}'.format(numb)
            i += 1
            list_in[i] = st
            i += 1
            list_in.insert(i,'"')
        i += 1
    str_out = remove_spaces(' '.join(list_in))
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
