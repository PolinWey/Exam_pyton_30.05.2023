import bynote3 as f
import bynote4


def run():
    input_from_user = ''
    while input_from_user != '7':
        bynote4.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            f.show('all')
        if input_from_user == '2':
            f.add()
        if input_from_user == '3':
            f.show('all')
            f.id_edit_del_show('del')
        if input_from_user == '4':
            f.show('all')
            f.id_edit_del_show('edit')
        if input_from_user == '5':
            f.show('date')
        if input_from_user == '6':
            f.show('id')
            f.id_edit_del_show('show')
        if input_from_user == '7':
            bynote4.goodbuy()
            break