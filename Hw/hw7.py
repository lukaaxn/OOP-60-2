import sqlite3
# Тетрадь типо
connect = sqlite3.connect('unsc.db')  # United Nations Security Council = unsc
# Ручка
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS unsc(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country Varchar (15) NOT NULL,
    capital Varchar (15) NOT NULL,
    square TEXT,
    population TEXT
    )
''')
connect.commit()

def create_unsc(country, capital, square, population):
     cursor.execute(
         'INSERT INTO unsc(country, capital, square, population) VALUES(?, ?, ?, ?)',
         (country, capital, square, population)
     )
     connect.commit()
     print('Страна принята!')

create_unsc('Russia', 'Moscow', '~17 098 246 km²', '~144 - 145m')
create_unsc('USA', 'Washington', '~9 833 517 km²', '~340 - 342m')
create_unsc('China', 'Beijing', '~9 596 961 km²', '~1 411 - 1 412m')
create_unsc('France', 'Paris', '~643 801 km²', '~65 - 66m')
create_unsc('Great Britain', 'London', '~243 610 km²', '~68 - 69m')

def read_unsc():
    cursor.execute('SELECT * FROM unsc')
    unsc =  cursor.fetchall()
    for i in unsc:
        print(f'ID: {i[0]}, COUNTRY: {i[1]}, CAPITAL: {i[2]}, SQUARE: {i[3]}, POPULATION: {i[4]}')
read_unsc()

def update_unsc():
    cursor.execute(
        'UPDATE unsc SET name = ? WHERE rowid = ?',
        (country, rowid)
    )
    connect.close()