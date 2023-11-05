"""
Module to display menu and working with functions from database.py
"""
import os
from typing import Union
from database import DataBase


db = DataBase()


class Menu:
    """
    Class to work with menu
    """
    def __init__(self):
        self.functions = {self.see_notes: 'See notes',
                          self.add_note: 'Add note',
                          self.delete_note: 'Delete note',
                          self.find_note: 'Find note'}
        self.note_dict = dict()

    def see_notes(self) -> None:
        """
        Function to get and display all notes from database
        :return:
        """
        self.clear_stdout()
        notes = db.get_all_notes()
        if not notes:
            print('Пока нет никаких заметок.\n'
                  'Вы можете добавить их с помощью функции под номером 2.\n')
        note_counter = 1
        for note in notes:
            note_id, note_title = note
            self.note_dict[note_counter] = note_id
            print(f"{note_counter}. {note_title}")
            note_counter += 1

    def add_note(self) -> None:
        """
        Menu function to add new note to database and show the result of adding
        :return:
        """
        self.clear_stdout()
        note_title = input('Введите название заметки\n')
        note_text = input('Введите текст заметки\n')
        if db.add_note(note_title, note_text):
            print('Заметка успешно добавлена')
        else:
            print('Заметка с таким названием уже существует!')

    def delete_note(self) -> None:
        """
        Menu function to delete note from database
        :return:
        """
        self.clear_stdout()
        note_id = input('Введите id заметки, чтобы её удалить\n'
                        'ID заметки можно посмотреть с помощью функции под номером 1\n')
        if not note_id.isdigit():
            print('Неправильный ввод, id записки должен быть числом.')
            return
        id_for_delete = self.note_dict.get(int(note_id))
        if id_for_delete:
            db.delete_note(int(id_for_delete))
            self.note_dict.pop(int(note_id))
            print('Заметка удалена')
        else:
            print('Такой заметки не существует')

    def find_note(self):
        """
        Menu function to search note by search query
        :return:
        """
        self.clear_stdout()
        query = input('Введите название заметки либо фразу для поиска\n')
        search_result = db.search_note_by_query(query)
        if search_result:
            print('По вашему запросу найдено:\n')
            for note in search_result:
                note_id, note_title, note_text = note
                print(f"{note_id}. {note_title} - {note_text}")
        else:
            print('По вашему запросу ничего не найдено.')

    def display_menu(self):
        """
        Display a menu where the key identifies the name of a function.
        :return:
        """
        menu = dict(enumerate(self.functions.items(), start=1))

        while True:
            for k, function in menu.items():
                print(f"{k})", function[1])
            selection = self.validate_selection(input('Выберите пункт меню\n'))
            if selection:
                menu[selection][0]()

    def validate_selection(self, selection: str) -> Union[bool, int]:
        """
        Validate user input
        If user input is not digit wait for another input
        If user input is a zero or user input more than amount of function wait for another input
        :param selection:
        :return:
        """
        if not selection.isdigit():
            print('Нужно ввести цифру.')
            return False
        if int(selection) == 0 or int(selection) > len(self.functions):
            print('Нужно ввести цифру, которая соответствует пункту в меню.')
            return False
        return int(selection)

    @staticmethod
    def clear_stdout() -> None:
        """
        Clear stdout in console
        :return:
        """
        os.system('cls')
