# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
import json
import datetime

def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note_id = len(notes) + 1
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "msg": msg, "date": date})
    save_notes()
    print("Заметка успешно сохранена")

def read_notes():
    filter_date = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    if not notes:
        print("Заметок нет")
        return
    if not filter_date:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
    else:
        filtered_notes = [note for note in notes if note["date"].startswith(filter_date)]
        if filtered_notes:
            for note in filtered_notes:
                print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
        else:
            print("Заметок с указанной датой нет")


def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input(f"Введите новый заголовок заметки ({note['title']}): ")
            msg = input(f"Введите новое тело заметки ({note['msg']}): ")
            if title:
                note["title"] = title
            if msg:
                note["msg"] = msg
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована")
            return
    print(f"Заметка с id {note_id} не найдена")

def delete_note():
    note_id = int(input("Введите id заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена")
            return
    print(f"Заметка с id {note_id} не найдена")

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

if __name__ == "__main__":
    notes = load_notes()
    while True:
        command = input("Введите команду:\n1.Добавить\n2.Прочитать\n3.Редактировать\n4.Удалить\n5.Выход\n ")
        if command == "1":
            add_note()
        elif command == "2":
            read_notes()
        elif command == "3":
            edit_note()
        elif command == "4":
            delete_note()
        elif command == "5":
            break
        else:
            print("Неверная команда")


# from PyQt5 import QtWidgets   
# from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox 
# from PyQt5.QtCore import Qt,QTimer  
# import sys
# import datetime
# def aplic():
#     app=QApplication(sys.argv)
#     okno=window()
#     okno.show()
#     sys.exit(app.exec_())
#     if __name__ == "__main__":
#         aplic()
#         class window(QMainWindow):
#             def __init__(self):
#                 super(window,self)._init_()
#                 self.setWindowTitle("programs")
#                 self.setGeometry(400,400,600,300)
#                 self.text_date=QtWidgets.QLabel(self)
#                 self.text_date.adjustSize()
#                 self.text_date.move(10,52)

#                 self.text_time=QtWidgets.QLabel(self)
#                 self.text_time.setText("выберите время")
#                 self.text_time.adjustSize()
#                 self.text_time.move(10,103)

#                 self.date=QtWidgets.QDateEdit(self)
#                 self.date.move(100,50)
#                 self.date.adjustSize()

#                 self.time=QtWidgets.QTimeEdit(self)
#                 self.time.move(110,100)
#                 self.time.adjustSize()

#                 self.sodati=QtWidgets.QLineEdit(self)
#                 self.sodati.setGeometry(100,150,160,30)
#                 self.sodati.adjustSize()
#                 self.sodati.setPlaceholderText("введите событие")

#                 self.knopka=QtWidgets.QPushButton(self)
#                 self.knopka.move(210,80)
#                 self.knopka.setText("готово")
#                 self.knopka.adjustSize()



