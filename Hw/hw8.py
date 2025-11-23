import sqlite3

connect = sqlite3.connect('groups.db')
cursor = connect.cursor()

def create_table():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        song VARCHAR (20) NOT NULL,
        views INTEGER NOT NULL,
        group_id INTEGER NOT NULL,
        FOREIGN KEY(group_id) REFERENCES groups(id)
    )
    ''')

    connect.commit()
create_table()

def insert_test_db():
    cursor.executemany(
        'INSERT INTO groups (name) VALUES (?)',
        [
            ('BTS',),
            ('Cortis',),
            ('Pierce The Veil',),

        ]
    )

    cursor.executemany(
        'INSERT INTO songs (song, views, group_id) VALUES (?,?,?)',
        [
            ('Spine Breaker', 100000000, 1),
            ('Fashion', 24000000, 2),
            ('So Far So Fake', 4400000, 3),
            ('Idol', 1300000000, 1),
            ('Go', 28000000, 2),
            ('Spine Breaker', 326000000, 1),
            ('WARNING', 1000, 10)
        ]
    )
    connect.commit()
    print('Данные успешно добавлены!')
insert_test_db()

def get_groups_song():
    cursor.execute('''
    SELECT groups.name, songs.song, songs.views
    FROM groups FULL OUTER JOIN songs ON groups.id = songs.group_id
    ''')

    stars = cursor.fetchall()
    print(stars)
get_groups_song()

def get_group_huge_views():
    # MAX() MIN() AVG() COUNT() SUM()
    cursor.execute(
        'SELECT groups.name, MAX(songs.views) FROM groups INNER JOIN songs ON groups.id = songs.group_id'
    )
    stars = cursor.fetchall()
    print(stars)

get_group_huge_views()

def get_best_group():
    cursor.execute(
        '''
        SELECT name FROM groups WHERE id IN (
            SELECT group_id FROM songs
            WHERE views > 25000000
        );
        ''')
    stars = cursor.fetchall()
    print(stars)
get_best_group()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT groups.name, songs.song, songs.views
        FROM groups LEFT JOIN songs ON groups.id = songs.group_id
        ''')
    connect.commit()
create_my_view()

def get_groups():
    cursor.execute('SELECT * FROM my_view')
    stars = cursor.fetchall()
    print(stars)
get_groups()
connect.close()













