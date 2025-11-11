import sqlite3 as sql
import time

db = sql.connect("The_Messier_Dualis_Database")

def CreateTable(tablename):
    cursor = db.cursor()
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

def UpdateTable(tablename, messier, name, dist, date, types, const, mag, desc):
    cursor = db.cursor()
    
    update_table = f'''INSERT INTO {tablename}
    ( Messier_Number, Name, Distance, Discovery_Date, Object_Type, Constellation, Apparent_Magnitude, Description)
    VALUES ({messier}, {name}, {dist}, {date}, {types}, {const}, {mag}, {desc});
    '''

    cursor.execute(update_table)
    db.commit()

def DelRow(tablename, messier):
    cursor = db.cursor()
    
    del_row = f"DELETE FROM {tablename} WHERE Messier_Number = {messier};"

    cursor.execute(del_row)
    db.commit()

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
        tabname = str(input("Enter the Table name that you wish to create: "))
        CreateTable(tabname)
        time.sleep(1)
        print("Table Created!")
    
    elif (inp == 2):
        tabname = str(input("Enter the Table name that you wish to edit in: "))
        time.sleep(0.6)
        mesname = str(input("Please enter the Messier Number: "))
        time.sleep(0.6)
        objname = str(input("Enter the Name of the Messier Object: "))
        time.sleep(0.6)
        dist = int(input("Please enter the Distance of the Messier Object from Earth in Light-Years: "))
        time.sleep(0.6)
        objdate = str(input("Enter theDate that the object was discovered in (Format: DD-MM-YYYY): "))
        time.sleep(0.6)
        objtype = str(input("Please enter the Type of the Messier Object: "))
        time.sleep(0.6)
        constname = str(input("Please enter the name of the Constellation in which the Messier Object is located in: "))
        time.sleep(0.6)
        apmag = float(input("Please enter the Apparent Magnitude of the Messier Object: "))
        time.sleep(0.6)
        desc = str(input("Please enter a short Description of the Messier Object: "))
        time.sleep(0.6)
        UpdateTable(tabname, mesname, objname, dist, objdate, objtype, constname, apmag, desc)
        time.sleep(1)
        print("Table Updated!")

    elif (inp == 3):
        tabname = str(input("Enter the Table name that you wish to edit in: "))
        time.sleep(0.6)
        mesname = str(input("Please enter the Messier Number of the record: "))
        time.sleep(0.6)
        DelRow(tabname, mesname)
        time.sleep(1)
        print("Edition Complete!")
        
    elif (inp == 4):
        print("Exiting!...")
        time.sleep(1)
        break
    
db.close()