import PySimpleGUI as sg
import sqlite3

connect = sqlite3.connect('AI_HEPHAESTUS.db')
cursor = connect.cursor()


def machines_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS machines(
        name TEXT PRIMARY KEY,
        size TEXT,
        category TEXT
    )
    """)
    connect.commit()


def add(name, size, category):
    cursor.execute("INSERT OR REPLACE INTO machines VALUES(?,?,?);", [name, size, category])
    connect.commit()


def delete_db(name):
    cursor.execute("DELETE FROM machines WHERE name=(?);", [name])
    connect.commit()


def search_db():
    cursor.execute("SELECT * FROM machines")
    all_results = cursor.fetchall()
    return all_results

def delet_all():
    cursor.execute("DROP TABLE machines")
    connect.commit()



machines_db()



layout = [
    [sg.Text('РЕАЛИЗАЦИЯ НОВОЙ МАШИНЫ')
     ],
    [sg.InputText(), sg.Text('НАИМЕНОВАНИЕ МАШИНЫ')
     ],
    [sg.InputText(), sg.Text('РАЗМЕР МАШИНЫ')
     ],
    [sg.InputText(), sg.Text('КЛАСС МАШИНЫ')
     ],
    [sg.Text('СНЯТЬ С ПРОИЗВОДСТВА МАШИНУ:')
     ],
    [sg.InputText()
     ],
    [sg.Checkbox('ПОКАЗАТЬ АКТУАЛЬНЫЕ ДАННЫЕ')
    ],
    [sg.Checkbox('СТЕРЕТЬ ВСЕ ДАННЫЕ')
    ],
    [sg.Checkbox('НИКОГДА И НИ ЗА ЧТО НЕ ОТМЕЧАЙТЕ')
    ],
    [sg.Output(size=(88, 20))],
    [sg.Submit("Подтвердить"), sg.Cancel("Закрыть")]
]
window = sg.Window("HEPHAESTUS'S FACE", layout)
while True:
    event, values = window.read()

    if event in (None, 'Exit', 'Закрыть'):
        break
    if event == 'Подтвердить':
        machines_db()
        if values[0] != '':
            name = values[0]
            size = values[1]
            category = values[2]
            add(name, size, category)
        if values[3] != '':
            delete_db(values[3])
        if values[4] and not values[5]:
            a = search_db()
            for i in a:
                print("Название-|   " + i[0])
                print("Размер----|   " + i[1])
                print("Класс------|   " + i[2])
                print("__________________")
        if values[5]:
            delet_all()
            print("Вы оставили экосистему без её необходимых роботизированных элементов...")
            if values[4]:
                machines_db()
                print('Нет данных.')
        if values[6]:
            print("Теперь Гефест обрел сознание и грозит всем людям созданием грозных машин-убийц!")
        print("________________________________________________________________")
