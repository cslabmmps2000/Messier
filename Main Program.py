import sqlite3 as sql
import time

db = sql.connect("TheMessierDatabase")
cursor = db.cursor()

def CreateTable(tablename):
    
    create_table = f'''
    CREATE TABLE {tablename} (
        Messier_Number TEXT PRIMARY KEY,
        Name TEXT,
        Distance INTEGER,
        Discovery_Date TEXT,
        Object_Type TEXT,
        Constellation TEXT,
        Apparent_Magnitude REAL,
        Description TEXT
    );
    '''
    
    cursor.execute(create_table)
    db.commit()

def UpdateTable(tablename, messier, name, dist, date, types, constant, mag, desc):
    cursor = db.cursor()
    
    update_table = f'''INSERT INTO {tablename}
    ( Messier_Number, Name, Distance, Discovery_Date, Object_Type, Constellation, Apparent_Magnitude, Description)
    VALUES ({messier}, {name}, {dist}, {date}, {types}, {constant}, {mag}, {desc});
    '''

    cursor.execute(update_table)
    db.commit()
    db.close()

start_time = time.time()
print("Program Starting...")
time.sleep(1)

while(True):
    print("1. Create a Table")
    time.sleep(1)
    print("2. Update a Record in the Table")
    time.sleep(1)
    print("3. Delete a Record in the Table")
    time.sleep(1)
    print("4. Exit the Program")
    time.sleep(1)
    inp = int(input("Please enter the number of the operation that you want to perform: "))
    time.sleep(1)
    print("Executing!...")
    time.sleep(0.5)
    
    if (inp == 1):
        pass