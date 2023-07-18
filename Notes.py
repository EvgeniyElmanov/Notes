import json
import os
from datetime import datetime


def load_notes():
    """Загружает заметки из файла notes.json."""
    if not os.path.exists("notes.json"):
        return []

    with open("notes.json", "r") as file:
        notes = json.load(file)
    return notes


def save_notes(notes):
    """Сохраняет заметки в файл notes.json."""
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def create_note():
    """Создает новую заметку."""
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана!")


def display_notes():
    """Отображает все заметки."""
    if not notes:
        print("Нет заметок.")
        return

    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print(f"Тело заметки: {note['body']}")
        print()


def edit_note():
    """Редактирует существующую заметку."""
    note_id = int(input("Введите ID заметки для редактирования: "))

    for note in notes:
        if note["id"] == note_id:
            print(f"Редактирование заметки с ID {note_id}:")
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return

    print(f"Заметка с ID {note_id} не найдена.")


def delete_note():
    """Удаляет существующую заметку."""
    note_id = int(input("Введите ID заметки для удаления: "))

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return

    print(f"Заметка с ID {note_id} не найдена.")


def main():
    global notes
    notes = load_notes()

    while True:
        print("==== Консольное приложение Заметки ====")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выйти из приложения")
        choice = input("Введите номер действия: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            display_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()