import bynote
import notes
import bynote4

number = 10  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = bynote4.create_note(number)
    array = bynote.read_file()
    for notes in array:
        if notes.Note.get_id(note) == notes.Note.get_id(notes):
            notes.Note.set_id(note)
    array.append(note)
    bynote.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = bynote.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notes.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notes.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notes.Note.get_date(notes):
                print(notes.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = bynote.read_file()
    logic = True
    for notes in array:
        if id == notes.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = bynote4.create_note(number)
                notes.Note.set_title(notes, note.get_title())
                notes.Note.set_body(notes, note.get_body())
                notes.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(notes.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    bynote.write_file(array, 'a')