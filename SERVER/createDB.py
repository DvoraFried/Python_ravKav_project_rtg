import sqlite3 as sqlite_library

database = sqlite_library.connect(database="./ravKav_DB.sqlite")
cursor = database.cursor()
create_table_cards = '''CREATE TABLE IF NOT EXISTS cards
                (card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INT, 
                name_contract TEXT, 
                wallet INT);
'''

cursor.execute(create_table_cards)
create_table_contracts = '''CREATE TABLE IF NOT EXISTS contracts
                (name_contract TEXT, 
                price INT,
                PRIMARY KEY(name_contract));
'''

cursor.execute(create_table_contracts)
add_contract = '''INSERT OR REPLACE INTO contracts
                (name_contract, price) VALUES ('NORTH', 25);
'''
cursor.execute(add_contract)
add_contract = '''INSERT OR REPLACE INTO contracts
                (name_contract, price) VALUES ('CENTER', 40);
'''
cursor.execute(add_contract)
add_contract = '''INSERT OR REPLACE INTO contracts
                (name_contract, price) VALUES ('SOUTH', 30);
'''
cursor.execute(add_contract)

cursor.execute(add_contract)
add_contract = '''INSERT OR REPLACE INTO contracts
                (name_contract, price) VALUES ('NONE', 0);
'''
cursor.execute(add_contract)
database.commit()